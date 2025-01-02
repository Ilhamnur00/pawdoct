from app import db
from app.models import User
from werkzeug.security import generate_password_hash

def test_user_model(app):
    with app.app_context():
        user = User(
            username="testuser",
            email="testuser@example.com",
            password=generate_password_hash("TestPass@123"),
            phone="081298765432",
            gender="male",
            address="User Address"
        )
        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.filter_by(username="testuser").first()
        assert fetched_user is not None
        assert fetched_user.email == "testuser@example.com"