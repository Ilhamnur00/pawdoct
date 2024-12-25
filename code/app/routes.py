# Mengimpor berbagai modul dan kelas yang dibutuhkan
from app.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, DiagnosaForm, UpdateProfileForm
from app.models import db, User, Gejala, Penyakit, PenyakitGejala, Diagnosa  # Model dan objek untuk database
from flask_mail import Message  # Digunakan untuk mengirim email
from app import mail  # Import objek mail yang telah dikonfigurasi
from flask import Blueprint, render_template, redirect, url_for, flash, request  # Flask routing dan rendering
from flask_login import login_user, logout_user, current_user, login_required  # Mengelola sesi login
from werkzeug.security import generate_password_hash, check_password_hash  # Untuk hashing password

# Inisialisasi Blueprint untuk rute utama aplikasi
main_bp = Blueprint('main_bp', __name__)

# Fungsi untuk mengirim email reset password kepada pengguna
def send_reset_email(user):
    token = user.get_reset_token()  # Mendapatkan token reset password untuk pengguna
    msg = Message('Reset Your Password',  # Membuat pesan email
                  sender='noreply@pawdoct.my.id',  # Alamat pengirim
                  recipients=[user.email])  # Alamat penerima
    
    reset_url = f"{request.host_url}reset_password/{token}"  # Membuat URL reset password

    # Menyiapkan isi pesan email
    msg.body = f'''Hai {user.username},

Klik tautan berikut ini untuk mereset kata sandi akun Pawdoct anda!
{reset_url}

Salam,
Tim Pawdoct
'''
    mail.send(msg)  # Mengirim email

# Rute untuk halaman utama aplikasi
@main_bp.route('/')
def index():
    return render_template('index.html')  # Merender halaman utama

# Rute untuk halaman registrasi pengguna
@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()  # Membuat instance form registrasi
    if form.validate_on_submit():  # Memeriksa apakah form sudah valid
        # Memeriksa apakah email sudah terdaftar
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email sudah digunakan. Silakan gunakan email lain.', 'danger')  # Menampilkan pesan error
            return render_template('signup.html', form=form)  # Kembali ke halaman signup

        # Jika email belum digunakan, simpan data pengguna baru
        user = User(
            username=form.username.data,
            email=form.email.data,
            phone=form.phone.data,
            gender=form.gender.data,
            address=form.address.data
        )
        user.set_password(form.password.data)  # Menyimpan password yang sudah di-hash
        db.session.add(user)  # Menambahkan pengguna ke database
        db.session.commit()  # Menyimpan perubahan ke database

        login_user(user)  # Login pengguna setelah registrasi
        if current_user.is_authenticated:  # Memastikan pengguna berhasil login
            return redirect(url_for('main_bp.home'))  # Redirect ke halaman home
        else:
            flash('Login gagal setelah registrasi. Silakan login secara manual.', 'danger')  # Menampilkan pesan error
            return redirect(url_for('main_bp.login'))  # Redirect ke halaman login

    return render_template('signup.html', form=form)  # Merender halaman signup

# Rute untuk halaman login
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Jika pengguna sudah login
        flash('Anda sudah login!', 'info')  # Menampilkan pesan informasi
        return redirect(url_for('main_bp.home'))  # Redirect ke halaman home

    form = LoginForm()  # Membuat instance form login
    if form.validate_on_submit():  # Memeriksa apakah form sudah valid
        user = User.query.filter_by(username=form.username.data).first()  # Mencari pengguna berdasarkan username
        if user and user.check_password(form.password.data):  # Memeriksa apakah password valid
            login_user(user)  # Login pengguna
            flash('Login berhasil. Selamat datang kembali!', 'success')  # Menampilkan pesan sukses
            return render_template('login.html', form=form, redirect_url=url_for('main_bp.home'))  # Redirect ke home
        else:
            flash('Login gagal. Periksa username dan password Anda.', 'danger')  # Menampilkan pesan error

    return render_template('login.html', form=form, redirect_url=None)  # Merender halaman login

# Rute untuk halaman lupa password
@main_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()  # Membuat instance form lupa password
    if form.validate_on_submit():  # Memeriksa apakah form sudah valid
        user = User.query.filter_by(email=form.email.data).first()  # Mencari pengguna berdasarkan email
        if user:  # Jika pengguna ditemukan
            send_reset_email(user)  # Mengirim email reset password
            flash('Link reset password telah dikirim ke email Anda!', 'info')  # Menampilkan pesan sukses
            return redirect(url_for('main_bp.login'))  # Redirect ke halaman login
        else:
            flash('Email tidak ditemukan.', 'danger')  # Menampilkan pesan error
            return redirect(url_for('main_bp.forgot_password'))  # Tetap di halaman lupa password

    return render_template('forgot_password.html', form=form)  # Merender halaman lupa password

# Rute untuk halaman reset password
@main_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_token(token)  # Verifikasi token reset
    if user is None:  # Jika token tidak valid
        flash('Token tidak valid atau telah kedaluwarsa.', 'warning')  # Menampilkan pesan peringatan
        return redirect(url_for('main_bp.forgot_password'))  # Redirect ke halaman lupa password
    
    form = ResetPasswordForm()  # Membuat instance form reset password
    if form.validate_on_submit():  # Memeriksa apakah form sudah valid
        user.set_password(form.password.data)  # Mengatur password baru
        db.session.commit()  # Menyimpan perubahan ke database
        flash('Password Anda telah berhasil direset!', 'success')  # Menampilkan pesan sukses
        return redirect(url_for('main_bp.login'))  # Redirect ke halaman login

    return render_template('reset_password.html', form=form, token=token)  # Merender halaman reset password

# Rute untuk logout pengguna
@main_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Logout pengguna
    flash('Anda telah berhasil logout.', 'info')  # Menampilkan pesan sukses
    return redirect(url_for('main_bp.login'))  # Redirect ke halaman login

# Rute untuk halaman home setelah login
@main_bp.route('/home')
@login_required
def home():
    return render_template('home.html')  # Merender halaman home

# Rute untuk halaman diagnosa
@main_bp.route('/diagnosa', methods=['GET', 'POST'])
@login_required
def diagnosa():
    form = DiagnosaForm()  # Membuat instance form diagnosa
    gejala_list = Gejala.query.all()  # Mengambil semua gejala dari database
    if not gejala_list:  # Jika tidak ada gejala
        flash('Tidak ada gejala yang tersedia di database.', 'warning')  # Menampilkan pesan peringatan
        return redirect(url_for('main_bp.home'))  # Redirect ke halaman home
    
    form.gejala.choices = [(g.kode_gejala, g.gejala) for g in gejala_list]  # Mengisi pilihan checkbox dengan gejala

    if form.validate_on_submit():  # Memeriksa apakah form sudah valid
        # Mengambil data dari form
        nama_kucing = form.nama_kucing.data
        jenis_kelamin = form.jenis_kelamin.data
        gejala_dipilih = form.gejala.data  # List gejala yang dipilih

        # Proses Diagnosa
        hasil = []
        penyakit_list = Penyakit.query.all()  # Mengambil semua penyakit dari database
        for penyakit in penyakit_list:
            # Mengambil gejala yang terkait dengan penyakit ini
            gejala_penyakit = PenyakitGejala.query.filter_by(penyakit_id=penyakit.id).all()
            if not gejala_penyakit:
                continue

            total_bobot_penyakit = sum(
                g.bobot
                for g in Gejala.query.filter(Gejala.kode_gejala.in_([pg.kode_gejala for pg in gejala_penyakit])).all()
            )
            bobot_dipilih = sum(
                g.bobot
                for g in Gejala.query.filter(Gejala.kode_gejala.in_(gejala_dipilih)).all()
                if g.kode_gejala in [pg.kode_gejala for pg in gejala_penyakit]
            )

            persentase = (bobot_dipilih / total_bobot_penyakit) * 100 if total_bobot_penyakit > 0 else 0
            hasil.append({
                "penyakit": penyakit.nama_penyakit,
                "persentase": persentase,
                "deskripsi": penyakit.deskripsi
            })
        
        # Menyimpan hasil diagnosa ke database
        diagnosa = Diagnosa(
            nama_kucing=nama_kucing,
            jenis_kelamin=jenis_kelamin,
            hasil_diagnosa=", ".join([f"{h['penyakit']} ({h['persentase']:.2f}%)" for h in hasil]),
            gejala_dipilih=", ".join(gejala_dipilih),  # Menyimpan gejala yang dipilih
            user_id=current_user.id  # Menyimpan ID pengguna yang login
        )
        db.session.add(diagnosa)
        db.session.commit()  # Menyimpan perubahan ke database

        return redirect(url_for('main_bp.hasil_diagnosa', id=diagnosa.id))  # Redirect ke halaman hasil diagnosa

    return render_template('diagnosa.html', form=form)  # Merender halaman diagnosa

# Rute untuk halaman hasil diagnosa
@main_bp.route('/hasil_diagnosa/<int:id>', methods=['GET'])
@login_required
def hasil_diagnosa(id):
    diagnosa = Diagnosa.query.get_or_404(id)  # Mengambil diagnosa berdasarkan ID
    
    hasil = []
    gejala_nama = []
    hasil_diatas_20 = []

    for item in diagnosa.hasil_diagnosa.split(", "):
        nama_penyakit, persentase = item.rsplit(" (", 1)
        persentase = persentase.strip(")%")

        try:
            persentase_float = float(persentase)  # Mengkonversi persentase ke float
        except ValueError:
            persentase_float = 0  # Jika konversi gagal, set persentase menjadi 0

        hasil.append({
            "penyakit": nama_penyakit,
            "persentase": persentase_float,
        })

    return render_template('hasil_diagnosa.html', diagnosa=diagnosa, hasil=hasil)  # Merender halaman hasil diagnosa

# Rute untuk halaman profil pengguna
@main_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()  # Membuat instance form untuk update profil
    if form.validate_on_submit():  # Memeriksa apakah form sudah valid
        current_user.username = form.username.data  # Mengupdate username pengguna
        current_user.email = form.email.data  # Mengupdate email pengguna
        current_user.phone = form.phone.data  # Mengupdate nomor telepon pengguna
        current_user.gender = form.gender.data  # Mengupdate gender pengguna
        current_user.address = form.address.data  # Mengupdate alamat pengguna

        db.session.commit()  # Menyimpan perubahan ke database
        flash('Profil Anda telah diperbarui!', 'success')  # Menampilkan pesan sukses
        return redirect(url_for('main_bp.profile'))  # Redirect kembali ke halaman profil
    
    # Mengisi form dengan data pengguna saat ini
    form.username.data = current_user.username
    form.email.data = current_user.email
    form.phone.data = current_user.phone
    form.gender.data = current_user.gender
    form.address.data = current_user.address
    
    return render_template('profile.html', form=form)  # Merender halaman profil

# Rute untuk halaman yang menunjukkan riwayat diagnosa pengguna
@main_bp.route('/riwayat_diagnosa', methods=['GET'])
@login_required
def riwayat_diagnosa():
    diagnosa_list = Diagnosa.query.filter_by(user_id=current_user.id).all()  # Mengambil riwayat diagnosa pengguna
    return render_template('riwayat_diagnosa.html', diagnosa_list=diagnosa_list)  # Merender halaman riwayat diagnosa

# Rute untuk halaman detail riwayat diagnosa pengguna
@main_bp.route('/riwayat_diagnosa/<int:id>', methods=['GET'])
@login_required
def detail_riwayat_diagnosa(id):
    diagnosa = Diagnosa.query.get_or_404(id)  # Mengambil detail diagnosa berdasarkan ID
    return render_template('detail_riwayat_diagnosa.html', diagnosa=diagnosa)  # Merender halaman detail riwayat diagnosa
