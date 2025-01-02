from app.forms import RegistrationForm, LoginForm

def test_signup_form():
    """Test RegistrationForm validation."""
    form = RegistrationForm(username="quicktest", email="test@example.com", password="QuickPass@123", confirm_password="QuickPass@123", phone="08123456789", gender="male", address="Test Address")
    assert form.validate()

def test_login_form():
    """Test LoginForm validation."""
    form = LoginForm(username="quicktest", password="QuickPass@123")
    assert form.validate()
