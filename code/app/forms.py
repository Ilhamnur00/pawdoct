from flask_wtf import FlaskForm  # Untuk membuat form dengan Flask-WTF
from wtforms import (StringField, PasswordField, SubmitField, EmailField, BooleanField, SelectField, SelectMultipleField, widgets)  # Import berbagai jenis field untuk form
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp  # Import validator untuk validasi input

# Form registrasi pengguna
class RegistrationForm(FlaskForm):
    # Field untuk username dengan validasi
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username tidak boleh kosong."),
            Length(min=3, message="Username harus minimal 3 karakter.")
        ]
    )
    # Field untuk email dengan validasi
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message="Email tidak boleh kosong."),
            Email(message="Masukkan email yang valid.")
        ]
    )
    # Field untuk password dengan validasi keamanan
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Password tidak boleh kosong."),
            Length(min=8, message="Password harus minimal 8 karakter."),
            Regexp(
                r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
                message="Password harus mengandung huruf, angka, dan karakter spesial."
            )
        ]
    )
    # Field untuk konfirmasi password
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(message="Konfirmasi password harus diisi."),
            EqualTo('password', message="Konfirmasi password tidak cocok.")
        ]
    )
    # Field untuk nomor telepon dengan validasi
    phone = StringField(
        'Phone Number',
        validators=[
            DataRequired(message="Nomor telepon tidak boleh kosong."),
            Length(min=10, max=15, message="Nomor telepon harus antara 10 hingga 15 digit."),
            Regexp(r'^[0-9]+$', message="Nomor telepon hanya boleh berisi angka.")
        ]
    )
    # Field untuk memilih gender
    gender = SelectField(
        'Gender',
        choices=[('male', 'Male'), ('female', 'Female')],
        validators=[DataRequired(message="Pilih jenis kelamin.")]
    )
    # Field untuk alamat dengan validasi panjang
    address = StringField(
        'Address',
        validators=[
            DataRequired(message="Alamat tidak boleh kosong."),
            Length(min=5, max=255, message="Alamat harus antara 5 hingga 255 karakter.")
        ]
    )
    # Tombol untuk mengirim form
    submit = SubmitField('Register')

# Form login pengguna
class LoginForm(FlaskForm):
    # Field untuk username
    username = StringField('Username', validators=[DataRequired()])
    # Field untuk password
    password = PasswordField('Password', validators=[DataRequired()])
    # Tombol login
    submit = SubmitField('Login')

# Form untuk lupa password
class ForgotPasswordForm(FlaskForm):
    # Field untuk email
    email = EmailField('Email', validators=[DataRequired(), Email()])
    # Tombol untuk mengirim link reset password
    submit = SubmitField('Send Reset Link')

# Form untuk reset password
class ResetPasswordForm(FlaskForm):
    # Field untuk password baru
    password = PasswordField('New Password', validators=[DataRequired()])
    # Field untuk konfirmasi password baru
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    # Tombol reset password
    submit = SubmitField('Reset Password')

# Form diagnosa penyakit pada kucing
class DiagnosaForm(FlaskForm):
    # Field untuk nama kucing
    nama_kucing = StringField('Nama Kucing', validators=[DataRequired()])
    # Field untuk memilih jenis kelamin kucing
    jenis_kelamin = SelectField(
        'Jenis Kelamin',
        choices=[('jantan', 'Jantan'), ('betina', 'Betina')],
        validators=[DataRequired()]
    )
    # Field untuk memilih gejala (dengan checkbox)
    gejala = SelectMultipleField(
        'Gejala',
        choices=[],  # Pilihan akan diisi dari route
        coerce=str,  # Pastikan tipe data sesuai
        widget=widgets.ListWidget(prefix_label=False),  # Menampilkan sebagai daftar
        option_widget=widgets.CheckboxInput()  # Checkbox untuk tiap opsi
    )
    # Tombol diagnosa
    submit = SubmitField('Diagnosa')

# Form untuk memperbarui profil pengguna
class UpdateProfileForm(FlaskForm):
    # Field untuk username
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username tidak boleh kosong."),
            Length(min=3, max=50, message="Username harus antara 3 hingga 50 karakter.")
        ]
    )
    # Field untuk nomor telepon
    phone = StringField(
        'Phone',
        validators=[
            DataRequired(message="Nomor telepon tidak boleh kosong."),
            Length(min=10, max=15, message="Nomor telepon harus antara 10 hingga 15 digit."),
            Regexp(r'^[0-9]+$', message="Nomor telepon hanya boleh berisi angka.")
        ]
    )
    # Field untuk memilih gender
    gender = SelectField(
        'Gender',
        choices=[('male', 'Male'), ('female', 'Female')],
        validators=[DataRequired(message="Pilih jenis kelamin.")]
    )
    # Field untuk alamat
    address = StringField(
        'Address',
        validators=[
            DataRequired(message="Alamat tidak boleh kosong."),
            Length(min=5, max=255, message="Alamat harus antara 5 hingga 255 karakter.")
        ]
    )
    # Field untuk password saat ini (untuk keamanan)
    current_password = PasswordField(
        'Current Password',
        validators=[DataRequired(message="Password saat ini harus diisi.")]
    )
    # Tombol untuk memperbarui profil
    submit = SubmitField('Update Profile')

# Form untuk reset password (dengan nama duplikat - mungkin perlu dihapus jika tidak digunakan)
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
