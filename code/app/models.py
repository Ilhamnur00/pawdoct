from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime
from app import db

class User(db.Model, UserMixin):
    """Model untuk tabel pengguna."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True) 
    gender = db.Column(db.String(10), nullable=True) 
    address = db.Column(db.Text, nullable=True) 

    def set_password(self, password):
        """Meng-hash password pengguna sebelum disimpan."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Memeriksa kecocokan password yang diinput dengan hash yang tersimpan."""
        return check_password_hash(self.password, password)

    def __repr__(self):
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
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        """Memverifikasi token reset password."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=1800)  # Sesuaikan waktu kedaluwarsa di sini
            user_id = data['user_id']
        except Exception:
            return None
        return User.query.get(user_id)

class Gejala(db.Model):
    """Model untuk tabel gejala."""
    __tablename__ = 'gejala'
    id = db.Column(db.Integer, primary_key=True)
    kode_gejala = db.Column(db.String(10), unique=True, nullable=False)
    gejala = db.Column(db.String(255), nullable=False)
    bobot = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Gejala {self.kode_gejala}: {self.gejala}>"
    
class Penyakit(db.Model):
    """Model untuk tabel penyakit."""
    __tablename__ = 'penyakit'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nama_penyakit = db.Column(db.String(255), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    solusi = db.Column(db.Text, nullable=True)  # Tambahkan kolom solusi

    # Relasi ke gejala melalui tabel penyakit_gejala
    gejala = db.relationship('PenyakitGejala', backref='penyakit', lazy=True)

    def __repr__(self):
        return f"<Penyakit {self.nama_penyakit}>"

class PenyakitGejala(db.Model):
    """Model untuk tabel relasi antara penyakit dan gejala."""
    __tablename__ = 'penyakit_gejala'
    id = db.Column(db.Integer, primary_key=True)
    penyakit_id = db.Column(db.Integer, db.ForeignKey('penyakit.id'), nullable=False)
    kode_gejala = db.Column(db.String(10), db.ForeignKey('gejala.kode_gejala'), nullable=False)

    def __repr__(self):
        return f"<PenyakitGejala PenyakitID: {self.penyakit_id}, Gejala: {self.kode_gejala}>"

class Diagnosa(db.Model):
    """Model untuk tabel diagnosa."""
    __tablename__ = 'diagnosa'
    id = db.Column(db.Integer, primary_key=True)
    nama_kucing = db.Column(db.String(255), nullable=False)
    jenis_kelamin = db.Column(db.String(10), nullable=False)
    hasil_diagnosa = db.Column(db.Text, nullable=False)  # Simpan hasil diagnosa dalam format string
    gejala_dipilih = db.Column(db.String(255), nullable=False)  # Menyimpan gejala yang dipilih
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)  # Simpan tanggal diagnosa
    
    # Relasi ke pengguna
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref='diagnosa', lazy=True)

    def __repr__(self):
        return f"<Diagnosa {self.nama_kucing}: {self.hasil_diagnosa}>"
