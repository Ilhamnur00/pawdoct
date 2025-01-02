import pytest
from app import create_app, db
from app.models import User, Gejala, Penyakit, PenyakitGejala
from werkzeug.security import generate_password_hash   

@pytest.fixture(scope="module")
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })
    
    with app.app_context():
        db.create_all()  # Membuat semua tabel di database in-memory
        yield app
        db.session.remove()
        db.drop_all()  # Menghapus semua data setelah pengujian selesai

@pytest.fixture(scope="module")
def client(app):
    return app.test_client()  # Menggunakan client untuk pengujian API

@pytest.fixture(scope="function")
def setup_data(app):
    with app.app_context():
        # Membuat user
        user = User(
            username="quicktest1",
            email="quicktest1@example.com",
            password=generate_password_hash("QuickPass@1234"),
            phone="08123456789",
            gender="male",
            address="Test Address"
        )
        db.session.add(user)

        # Menambahkan gejala
        gejala1 = Gejala(kode_gejala="G001", gejala="Gejala 1", bobot=5)
        gejala2 = Gejala(kode_gejala="G002", gejala="Gejala 2", bobot=3)
        db.session.add_all([gejala1, gejala2])

        # Menambahkan penyakit
        penyakit = Penyakit(nama_penyakit="Penyakit A", deskripsi="Deskripsi Penyakit A")
        db.session.add(penyakit)

        # Menghubungkan gejala dengan penyakit
        penyakit_gejala1 = PenyakitGejala(penyakit_id=1, kode_gejala="G001")
        penyakit_gejala2 = PenyakitGejala(penyakit_id=1, kode_gejala="G002")
        db.session.add_all([penyakit_gejala1, penyakit_gejala2])

        db.session.commit()  # Simpan semua perubahan ke database

@pytest.fixture(scope="function", autouse=True)
def reset_database(app):
    """Reset database sebelum setiap test, hapus data dan buat ulang tabel."""
    with app.app_context():
        db.session.remove()
        db.drop_all()  # Hapus tabel jika sudah ada
        db.create_all()  # Buat tabel ulang