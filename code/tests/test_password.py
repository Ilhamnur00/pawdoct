from werkzeug.security import check_password_hash, generate_password_hash

def test_password_hashing():
    """Test password hashing and verification."""
    password = "QuickPass@123"
    hashed_password = generate_password_hash(password)
    assert check_password_hash(hashed_password, password)
