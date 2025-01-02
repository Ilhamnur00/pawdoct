import pytest
from app import db
from app.models import User

# Fixture untuk user baru
@pytest.fixture
def new_user():
    """Fixture untuk membuat user baru untuk testing"""
    user = User(username="testuser", email="test@example.com", password="testpassword")
    db.session.add(user)
    db.session.commit()
    return user

def test_user_model(new_user):
    """Test untuk memastikan user bisa disimpan dengan benar"""
    user = new_user
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.password == 'testpassword'  # Harus disesuaikan dengan cara penyimpanan password, misalnya hash

def test_user_repr(new_user):
    """Test untuk __repr__ method pada User model"""
    user = new_user
    assert repr(user) == '<User testuser>'

def test_user_query(new_user):
    """Test untuk memastikan query user berhasil"""
    user = new_user
    queried_user = User.query.filter_by(username='testuser').first()
    assert queried_user is not None
    assert queried_user.username == user.username
    assert queried_user.email == user.email

def test_user_unique_constraint():
    """Test untuk memastikan constraint unik pada username dan email"""
    user1 = User(username="uniqueuser", email="unique@example.com", password="password1")
    db.session.add(user1)
    db.session.commit()

    # Menguji bahwa username dan email harus unik
    user2 = User(username="uniqueuser", email="another@example.com", password="password2")
    db.session.add(user2)
    try:
        db.session.commit()  # Harus gagal karena username sudah ada
    except Exception as e:
        assert 'UNIQUE constraint' in str(e)  # Error constraint unik

    user3 = User(username="newuser", email="unique@example.com", password="password3")
    db.session.add(user3)
    try:
        db.session.commit()  # Harus gagal karena email sudah ada
    except Exception as e:
        assert 'UNIQUE constraint' in str(e)  # Error constraint unik
