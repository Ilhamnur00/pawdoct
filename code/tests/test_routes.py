from app.models import User

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_registration_route(client, app):
    response = client.post("/signup", data={
        "username": "newuser2",
        "email": "newuser2@example.com",
        "password": "NewPass@12345",
        "confirm_password": "NewPass@12345",
        "phone": "08129876543",
        "gender": "female",
        "address": "New Address"
    }, follow_redirects=True)

    assert response.status_code == 200

    with app.app_context():
        user = User.query.filter_by(username="newuser2").first()
        assert user is not None
        assert user.email == "newuser2@example.com"
        assert user.phone == "08129876543"

    check_home_response = client.get("/home")
    assert check_home_response.status_code == 200
    
    check_diagnosa_response = client.get("/diagnosa")
    assert check_diagnosa_response.status_code == 302
    
    check_riwayat_response = client.get("/riwayat")
    assert check_riwayat_response.status_code == 200
    
    check_profile_response = client.get("/profile")
    assert check_profile_response.status_code == 200