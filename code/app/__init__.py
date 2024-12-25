from flask import Flask  # Untuk membuat aplikasi Flask
from flask_sqlalchemy import SQLAlchemy  # Untuk menghubungkan ke database
from flask_migrate import Migrate  # Untuk menangani migrasi database
from flask_login import LoginManager  # Untuk mengatur login pengguna
from flask_mail import Mail  # Untuk mengirim email
from dotenv import load_dotenv  # Untuk membaca file .env
load_dotenv()  # Memuat variabel dari file .env
import os  # Untuk mengakses variabel lingkungan

# Inisialisasi ekstensi (fitur tambahan Flask)
db = SQLAlchemy()  # Menghubungkan aplikasi dengan database
migrate = Migrate()  # Mengelola perubahan pada database
login_manager = LoginManager()  # Mengatur proses login/logout
mail = Mail()  # Mengatur pengiriman email

# Menentukan halaman login default jika pengguna belum login
login_manager.login_view = 'main_bp.login'

def create_app():
    # Membuat objek aplikasi Flask
    app = Flask(__name__, static_folder="static")  # Menentukan folder untuk file statis (CSS, JS, gambar)

    # Mengatur konfigurasi aplikasi dari file .env
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")  # Kunci rahasia untuk keamanan aplikasi
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  # Alamat database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Menonaktifkan fitur pelacakan perubahan (lebih hemat memori)
    
    # Konfigurasi pengiriman email
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')  # Alamat server email
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))  # Port server email
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'  # Menggunakan keamanan TLS
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Nama pengguna email
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Kata sandi email
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')  # Alamat pengirim default untuk email

    # Menghubungkan ekstensi dengan aplikasi Flask
    db.init_app(app)  # Menghubungkan database
    migrate.init_app(app, db)  # Mengelola migrasi database
    login_manager.init_app(app)  # Mengatur login/logout pengguna
    mail = Mail(app)  # Mengaktifkan pengiriman email

    # Mengimpor dan mendaftarkan blueprint
    from .routes import main_bp  # Blueprint adalah grup route
    app.register_blueprint(main_bp)  # Mendaftarkan blueprint ke aplikasi

    return app  # Mengembalikan objek aplikasi yang sudah dikonfigurasi

# Fungsi untuk mengambil data pengguna berdasarkan ID (diperlukan oleh Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # Menghindari kesalahan import melingkar
    return User.query.get(int(user_id))  # Mencari pengguna berdasarkan ID di database
