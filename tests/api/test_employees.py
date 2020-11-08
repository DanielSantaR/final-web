import json

PREFIX = "/api/employees"


def test_create_carrier(test_app_with_db):
    data = {
        "identity_card": "1040050021",
        "names": "Daniel",
        "surnames": "Santa Rendón",
        "phone": "3192884146",
        "email": "daniel.santar@udea.edu.co",
        "username": "daniel",
        "is_active": True,
        "role": "manager",
        "password": "daniel",
    }
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 201
    response = response.json()
    assert response["identity_card"] == data["identity_card"]
    assert response["names"] == data["names"]
    assert response["surnames"] == data["surnames"]
    assert response["phone"] == data["phone"]
    assert response["email"] == data["email"]
    assert response["username"] == data["username"]
    assert response["is_active"] == data["is_active"]
    assert response["role"] == data["role"]
    assert "password" not in response
