from app.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, DiagnosaForm, UpdateProfileForm
from app.models import db, User, Gejala, Penyakit, PenyakitGejala, Diagnosa
from flask_mail import Message
from app import mail
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


# Inisialisasi Blueprint
main_bp = Blueprint('main_bp', __name__)

def send_reset_email(user):
    token = user.get_reset_token()  # Memanggil metode untuk mendapatkan token reset
    msg = Message('PAWDOCT - Reset Your Password',
                  sender='noreply@pawdoct.my.id',
                  recipients=[user.email])
    
    # Menggunakan request.host_url untuk mendapatkan URL yang benar
    reset_url = f"{request.host_url}reset_password/{token}"
    
    # Format pesan email sesuai permintaan
    msg.body = f'''Hai {user.username},

Klik tautan berikut ini untuk mereset kata sandi akun Pawdoct anda!
{reset_url}

Salam,
Tim Pawdoct
'''
    mail.send(msg)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Cek apakah email sudah digunakan
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email sudah digunakan. Silakan gunakan email lain.', 'danger')
            return render_template('signup.html', form=form)

        # Jika email belum digunakan, simpan data
        user = User(
            username=form.username.data,
            email=form.email.data,
            phone=form.phone.data,
            gender=form.gender.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        # Login pengguna setelah registrasi
        login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('main_bp.home'))  # Redirect ke home
        else:
            flash('Login gagal setelah registrasi. Silakan login secara manual.', 'danger')
            return redirect(url_for('main_bp.login'))  # Redirect ke login

    return render_template('signup.html', form=form)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Anda sudah login!', 'info')
        return redirect(url_for('main_bp.home'))  # Jika sudah login, arahkan ke home

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)  # Login pengguna
            flash('Login berhasil. Selamat datang kembali!', 'success')
            return render_template('login.html', form=form, redirect_url=url_for('main_bp.home'))
        else:
            flash('Login gagal. Periksa username dan password Anda.', 'danger')

    return render_template('login.html', form=form, redirect_url=None)

@main_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
            flash('Link reset password telah dikirim ke email Anda!', 'info')
            return redirect(url_for('main_bp.login'))  # Langsung lakukan redirect ke halaman login
        else:
            flash('Email tidak ditemukan.', 'danger')
            return redirect(url_for('main_bp.forgot_password'))  # Tetap di halaman forgot password untuk mencoba lagi
    return render_template('forgot_password.html', form=form)

@main_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('Token tidak valid atau telah kedaluwarsa.', 'warning')
        return redirect(url_for('main_bp.forgot_password'))
    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session .commit()
        flash('Password Anda telah berhasil direset!', 'success')
        return redirect(url_for('main_bp.login'))
    return render_template('reset_password.html', form =form, token=token)
def set_password(self, password):
    self.password = generate_password_hash(password)

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah berhasil logout.', 'info')
    return redirect(url_for('main_bp.login'))

@main_bp.route('/home')
@login_required
def home():
    return render_template('home.html')

@main_bp.route('/diagnosa', methods=['GET', 'POST'])
@login_required
def diagnosa():
    form = DiagnosaForm()
    gejala_list = Gejala.query.all()
    if not gejala_list:
        flash('Tidak ada gejala yang tersedia di database.', 'warning')
        return redirect(url_for('main_bp.home'))
    
    # Isi pilihan untuk checkbox
    form.gejala.choices = [(g.kode_gejala, g.gejala) for g in gejala_list]
    
    if form.validate_on_submit():
        nama_kucing = form.nama_kucing.data
        jenis_kelamin = form.jenis_kelamin.data
        gejala_dipilih = form.gejala.data  # List kode_gejala yang dipilih

        # Proses Diagnosa
        hasil = []
        penyakit_list = Penyakit.query.all()
        for penyakit in penyakit_list:
            # Ambil semua gejala terkait penyakit ini
            gejala_penyakit = PenyakitGejala.query.filter_by(penyakit_id=penyakit.id).all()
            if not gejala_penyakit:
                continue

            # Hitung total bobot untuk gejala yang dipilih
            total_bobot_penyakit = sum(
                g.bobot
                for g in Gejala.query.filter(Gejala.kode_gejala.in_([pg.kode_gejala for pg in gejala_penyakit])).all()
            )
            bobot_dipilih = sum(
                g.bobot
                for g in Gejala.query.filter(Gejala.kode_gejala.in_(gejala_dipilih)).all()
                if g.kode_gejala in [pg.kode_gejala for pg in gejala_penyakit]
            )

            # Hitung persentase berdasarkan bobot
            persentase = (bobot_dipilih / total_bobot_penyakit) * 100 if total_bobot_penyakit > 0 else 0
            hasil.append({
                "penyakit": penyakit.nama_penyakit,
                "persentase": persentase,
                "deskripsi": penyakit.deskripsi
            })
        hasil_diagnosa = ", ".join(
            [f"{h['penyakit']} ({h['persentase']:.2f}%)" for h in hasil]
        )

        # Simpan ke database
        diagnosa = Diagnosa(
            nama_kucing=nama_kucing,
            jenis_kelamin=jenis_kelamin,
            hasil_diagnosa=hasil_diagnosa,
            gejala_dipilih=", ".join(gejala_dipilih),  # Menyimpan gejala yang dipilih
            user_id=current_user.id  # Kaitkan diagnosa dengan pengguna yang login
        )
        db.session.add(diagnosa)
        db.session.commit()

        # Redirect ke hasil diagnosa dengan ID
        return redirect(url_for('main_bp.hasil_diagnosa', id=diagnosa.id))
    
    return render_template('diagnosa.html', form=form)

@main_bp.route('/hasil_diagnosa/<int:id>', methods=['GET'])
@login_required
def hasil_diagnosa(id):
    diagnosa = Diagnosa.query.get_or_404(id)

    # Memproses hasil diagnosa untuk mengambil penyakit dengan persentase tertinggi
    hasil = []
    gejala_nama = []
    hasil_diatas_20 = []

    # Menyusun hasil diagnosa dan gejala yang dipilih
    for item in diagnosa.hasil_diagnosa.split(", "):
        nama_penyakit, persentase = item.rsplit(" (", 1)
        persentase = persentase.strip(")%")
        
        try:
            persentase_float = float(persentase)  # Konversi ke float setelah membersihkan string
        except ValueError:
            persentase_float = 0  # Jika gagal konversi, set persentase menjadi 0 (nilai default)

        hasil.append({
            "penyakit": nama_penyakit,
            "persentase": persentase_float,
        })

    # Menentukan gejala yang dipilih dan penyakit dengan persentase di atas 20%
    gejala_nama = []
    for gejala_kode in diagnosa.gejala_dipilih.split(", "):  # Ambil kode gejala yang dipilih
        gejala = Gejala.query.filter_by(kode_gejala=gejala_kode).first()
        if gejala:
            gejala_nama.append(gejala.gejala)  # Ambil nama gejala

    hasil_diatas_20 = [h for h in hasil if h["persentase"] > 20]  # Hanya penyakit dengan persentase > 20%

    # Menentukan penyakit dengan persentase tertinggi
    if hasil:
        penyakit_tertinggi = max(hasil, key=lambda x: x['persentase'])
        diagnosa.penyakit_tertinggi = penyakit_tertinggi['penyakit']
        
        # Ambil solusi untuk penyakit yang memiliki persentase tertinggi
        solusi_tertinggi = Penyakit.query.filter_by(nama_penyakit=penyakit_tertinggi['penyakit']).first().solusi
        db.session.commit()  # Menyimpan perubahan ke database

    return render_template('hasil_diagnosa.html', diagnosa=diagnosa, hasil=hasil, gejala_nama=gejala_nama, hasil_diatas_20=hasil_diatas_20, solusi_tertinggi=solusi_tertinggi)

@main_bp.route('/riwayat')
@login_required
def riwayat():
    # Mengambil semua riwayat diagnosa yang terkait dengan user yang sedang login
    diagnosa_list = Diagnosa.query.filter_by(user_id=current_user.id).order_by(Diagnosa.tanggal.desc()).all()

    # Proses untuk menampilkan nama penyakit dengan persentase tertinggi dalam format yang sesuai
    for diagnosa in diagnosa_list:
        if diagnosa.hasil_diagnosa:
            # Memisahkan penyakit dan persentase dari hasil_diagnosa
            hasil = []
            for item in diagnosa.hasil_diagnosa.split(", "):
                nama_penyakit, persentase = item.rsplit(" (", 1)
                persentase = persentase.strip(")%")
                try:
                    persentase_float = float(persentase)
                except ValueError:
                    persentase_float = 0
                hasil.append({
                    "penyakit": nama_penyakit,
                    "persentase": persentase_float,
                })

            # Menentukan penyakit dengan persentase tertinggi
            if hasil:
                penyakit_tertinggi = max(hasil, key=lambda x: x['persentase'])
                diagnosa.penyakit_tertinggi = f"{penyakit_tertinggi['penyakit']} ({penyakit_tertinggi['persentase']:.2f}%)"
                db.session.commit()  # Menyimpan perubahan ke database

    return render_template('riwayat.html', diagnosa_list=diagnosa_list)

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UpdateProfileForm(obj=current_user)  # Prefill data pengguna saat ini

    if form.validate_on_submit():
        # Verifikasi password
        if not current_user.check_password(form.current_password.data):
            flash("Password salah. Tidak dapat mengubah profil.", "danger")
            return redirect(url_for('main_bp.edit_profile'))  # Redirect ke halaman edit profil

        # Cek apakah ada perubahan pada data
        if (form.username.data == current_user.username and
            form.phone.data == current_user.phone and
            form.gender.data == current_user.gender and
            form.address.data == current_user.address):
            flash("Tidak ada perubahan yang disimpan", "danger")
            return redirect(url_for('main_bp.edit_profile'))  # Redirect jika tidak ada perubahan

        # Perbarui data pengguna jika ada perubahan
        try:
            current_user.username = form.username.data
            current_user.phone = form.phone.data
            current_user.gender = form.gender.data
            current_user.address = form.address.data
            db.session.commit()  # Simpan perubahan ke database

            flash("Profil berhasil diperbarui!", "success")
            return redirect(url_for('main_bp.edit_profile'))  # Redirect ke halaman edit profil untuk menampilkan pesan
        except Exception as e:
            db.session.rollback()
            flash(f"Terjadi kesalahan: {e}", "danger")
            return redirect(url_for('main_bp.edit_profile'))  # Redirect ke halaman edit profil

    return render_template('edit_profile.html', form=form)
