from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username tidak boleh kosong."),
            Length(min=3, message="Username harus minimal 3 karakter.")
        ]
    )
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message="Email tidak boleh kosong."),
            Email(message="Masukkan email yang valid.")
        ]
    )
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
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(message="Konfirmasi password harus diisi."),
            EqualTo('password', message="Konfirmasi password tidak cocok.")
        ]
    )
    phone = StringField(
        'Phone Number',
        validators=[
            DataRequired(message="Nomor telepon tidak boleh kosong."),
            Length(min=10, max=15, message="Nomor telepon harus antara 10 hingga 15 digit."),
            Regexp(r'^[0-9]+$', message="Nomor telepon hanya boleh berisi angka.")
        ]
    )
    gender = SelectField(
        'Gender',
        choices=[('male', 'Laki-laki'), ('female', 'Perempuan')],
        validators=[DataRequired(message="Pilih jenis kelamin.")]
    )
    address = StringField(
        'Address',
        validators=[
            DataRequired(message="Alamat tidak boleh kosong."),
            Length(min=5, max=255, message="Alamat harus antara 5 hingga 255 karakter.")
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ForgotPasswordForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Reset Link')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class DiagnosaForm(FlaskForm):
    nama_kucing = StringField('Nama Kucing', validators=[DataRequired()])
    jenis_kelamin = SelectField(
        'Jenis Kelamin',
        choices=[('jantan', 'Jantan'), ('betina', 'Betina')],
        validators=[DataRequired()]
    )
    gejala = SelectMultipleField(
        'Gejala',
        choices=[],  # Akan diisi di route
        coerce=str,  # Pastikan ini sesuai dengan tipe `kode_gejala`
        widget=widgets.ListWidget(prefix_label=False),  # Membuat checkbox
        option_widget=widgets.CheckboxInput()
    )
    submit = SubmitField('Diagnosa')

class UpdateProfileForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username tidak boleh kosong."),
            Length(min=3, max=50, message="Username harus antara 3 hingga 50 karakter.")
        ]
    )
    phone = StringField(
        'Phone',
        validators=[
            DataRequired(message="Nomor telepon tidak boleh kosong."),
            Length(min=10, max=15, message="Nomor telepon harus antara 10 hingga 15 digit."),
            Regexp(r'^[0-9]+$', message="Nomor telepon hanya boleh berisi angka.")
        ]
    )
    gender = SelectField(
        'Gender',
        choices=[('male', 'Laki-laki'), ('female', 'Perempuan')],
        validators=[DataRequired(message="Pilih jenis kelamin.")]
    )
    address = StringField(
        'Address',
        validators=[
            DataRequired(message="Alamat tidak boleh kosong."),
            Length(min=5, max=255, message="Alamat harus antara 5 hingga 255 karakter.")
        ]
    )
    current_password = PasswordField(
        'Current Password',
        validators=[DataRequired(message="Password saat ini harus diisi.")]
    )
    submit = SubmitField('Update Profile')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')