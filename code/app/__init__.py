from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
load_dotenv()
import os

# Inisialisasi ekstensi
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

login_manager.login_view = 'main_bp.login'

def create_app():
    # Inisialisasi aplikasi Flask
    app = Flask(__name__, static_folder="static")  # Mengatur folder static
    
    # Konfigurasi aplikasi
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Konfigurasi Flask-Mail
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    # Inisialisasi ekstensi dengan aplikasi
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main_bp.login'  # Tentukan route login
    
    mail = Mail(app)  # Inisialisasi Flask-Mail
    
    # Registrasi blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

# Loader untuk Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # Hindari import melingkar
    return User.query.get(int(user_id))
