from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pawdoct1.0'
db = SQLAlchemy(app)

# Pengguna
class Pengguna(db.Model):
    __tablename__ = 'pengguna'
    id_pengguna = db.Column(db.Integer, primary_key=True)
    nama_pengguna = db.Column(db.String(100), nullable=False)
    email_pengguna = db.Column(db.String(100), nullable=False, unique=True)
    password_pengguna = db.Column(db.String(255), nullable=False)
    hewan = db.relationship('Hewan', backref='pemilik', lazy=True)

# Hewan
class Hewan(db.Model):
    __tablename__ = 'hewan'
    id_hewan = db.Column(db.Integer, primary_key=True)
    nama_hewan = db.Column(db.String(100), nullable=False)
    jenis_kelamin = db.Column(db.String(10), nullable=False)
    id_pengguna = db.Column(db.Integer, db.ForeignKey('pengguna.id_pengguna'), nullable=False)
    hasil_diagnosa = db.relationship('HasilDiagnosa', backref='hewan', lazy=True)

# Gejala
class Gejala(db.Model):
    __tablename__ = 'gejala'
    id_gejala = db.Column(db.Integer, primary_key=True)
    nama_gejala = db.Column(db.String(100), nullable=False)
    point_gejala = db.Column(db.Integer)

# Relasi Many-to-Many antara Penyakit dan Gejala
penyakit_gejala = db.Table('penyakit_gejala',
    db.Column('id_penyakit', db.Integer, db.ForeignKey('penyakit.id_penyakit'), primary_key=True),
    db.Column('id_gejala', db.Integer, db.ForeignKey('gejala.id_gejala'), primary_key=True)
)

# Penyakit
class Penyakit(db.Model):
    __tablename__ = 'penyakit'
    id_penyakit = db.Column(db.Integer, primary_key=True)
    nama_penyakit = db.Column(db.String(100), nullable=False)
    persentase_gejala = db.Column(db.Float)
    gejala = db.relationship('Gejala', secondary=penyakit_gejala, backref=db.backref('penyakit', lazy=True))

# Hasil Diagnosa
class HasilDiagnosa(db.Model):
    __tablename__ = 'hasil_diagnosa'
    id_diagnosa = db.Column(db.Integer, primary_key=True)
    id_hewan = db.Column(db.Integer, db.ForeignKey('hewan.id_hewan'), nullable=False)
    id_penyakit = db.Column(db.Integer, db.ForeignKey('penyakit.id_penyakit'), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)
    besaran_presentase = db.Column(db.Float)
