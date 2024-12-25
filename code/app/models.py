from flask import current_app  # Mengambil instance aplikasi saat ini
from werkzeug.security import generate_password_hash, check_password_hash  # Untuk hash dan verifikasi password
from itsdangerous import URLSafeTimedSerializer as Serializer  # Untuk membuat dan memverifikasi token aman
from flask_login import UserMixin  # Untuk integrasi dengan Flask-Login
from datetime import datetime  # Untuk pengelolaan tanggal dan waktu
from app import db  # Menggunakan instance database dari aplikasi

# Model untuk tabel pengguna
class User(db.Model, UserMixin):
    """Model untuk tabel pengguna."""
    id = db.Column(db.Integer, primary_key=True)  # Primary key untuk identifikasi pengguna
    username = db.Column(db.String(50), unique=True, nullable=False)  # Username unik
    password = db.Column(db.String(255), nullable=False)  # Password yang sudah di-hash
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email unik
    phone = db.Column(db.String(20), nullable=True)  # Nomor telepon 
    gender = db.Column(db.String(10), nullable=True)  # Jenis kelamin 
    address = db.Column(db.Text, nullable=True)  # Alamat 

    def set_password(self, password):
        """Meng-hash password pengguna sebelum disimpan."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Memeriksa kecocokan password yang diinput dengan hash yang tersimpan."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        """Merepresentasikan objek pengguna sebagai string."""
        return f"<User {self.username}>"

    def update_profile(self, username=None, phone=None, gender=None, address=None):
        """Memperbarui profil pengguna."""
        if username:
            self.username = username
        if phone:
            self.phone = phone
        if gender:
            self.gender = gender
        if address:
            self.address = address

    def get_reset_token(self, expires_sec=1800):
        """Membuat token reset password dengan waktu kedaluwarsa."""
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})  # Mengembalikan token untuk user_id

    @staticmethod
    def verify_reset_token(token):
        """Memverifikasi token reset password."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=1800)  # Token hanya valid dalam 30 menit
            user_id = data['user_id']
        except Exception:
            return None  # Token tidak valid atau kedaluwarsa
        return User.query.get(user_id)  # Mengembalikan user berdasarkan user_id

# Model untuk tabel gejala
class Gejala(db.Model):
    """Model untuk tabel gejala."""
    __tablename__ = 'gejala'  # Nama tabel dalam database
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    kode_gejala = db.Column(db.String(10), unique=True, nullable=False)  # Kode gejala unik
    gejala = db.Column(db.String(255), nullable=False)  # Deskripsi gejala
    bobot = db.Column(db.Integer, nullable=False)  # Bobot gejala untuk diagnosa

    def __repr__(self):
        """Merepresentasikan objek gejala sebagai string."""
        return f"<Gejala {self.kode_gejala}: {self.gejala}>"

# Model untuk tabel penyakit
class Penyakit(db.Model):
    """Model untuk tabel penyakit."""
    __tablename__ = 'penyakit'  # Nama tabel dalam database
    __table_args__ = {'extend_existing': True}  # Memungkinkan perpanjangan tabel jika sudah ada
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    nama_penyakit = db.Column(db.String(255), nullable=False)  # Nama penyakit
    deskripsi = db.Column(db.Text, nullable=False)  # Deskripsi penyakit
    solusi = db.Column(db.Text, nullable=True)  # Solusi atau rekomendasi untuk penyakit

    # Relasi ke tabel penyakit_gejala
    gejala = db.relationship('PenyakitGejala', backref='penyakit', lazy=True)

    def __repr__(self):
        """Merepresentasikan objek penyakit sebagai string."""
        return f"<Penyakit {self.nama_penyakit}>"

# Model untuk relasi antara penyakit dan gejala
class PenyakitGejala(db.Model):
    """Model untuk tabel relasi antara penyakit dan gejala."""
    __tablename__ = 'penyakit_gejala'  # Nama tabel dalam database
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    penyakit_id = db.Column(db.Integer, db.ForeignKey('penyakit.id'), nullable=False)  # Foreign key ke penyakit
    kode_gejala = db.Column(db.String(10), db.ForeignKey('gejala.kode_gejala'), nullable=False)  # Foreign key ke gejala

    def __repr__(self):
        """Merepresentasikan objek relasi penyakit-gejala sebagai string."""
        return f"<PenyakitGejala PenyakitID: {self.penyakit_id}, Gejala: {self.kode_gejala}>"

# Model untuk tabel diagnosa
class Diagnosa(db.Model):
    """Model untuk tabel diagnosa."""
    __tablename__ = 'diagnosa'  # Nama tabel dalam database
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    nama_kucing = db.Column(db.String(255), nullable=False)  # Nama kucing yang didiagnosa
    jenis_kelamin = db.Column(db.String(10), nullable=False)  # Jenis kelamin kucing
    hasil_diagnosa = db.Column(db.Text, nullable=False)  # Hasil diagnosa dalam bentuk teks
    gejala_dipilih = db.Column(db.String(255), nullable=False)  # Gejala yang dipilih oleh pengguna
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)  # Tanggal diagnosa

    # Relasi ke tabel pengguna
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Foreign key ke pengguna
    user = db.relationship('User', backref='diagnosa', lazy=True)  # Membuat relasi dengan pengguna

    def __repr__(self):
        """Merepresentasikan objek diagnosa sebagai string."""
        return f"<Diagnosa {self.nama_kucing}: {self.hasil_diagnosa}>"
