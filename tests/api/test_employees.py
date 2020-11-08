import json

PREFIX = "/api/employees"

DATA = {
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


def test_not_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_create_carrier(test_app_with_db):
    # First record
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(DATA),)

    assert response.status_code == 201
    response = response.json()
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "password" not in response

    # Second record
    data = {
        "identity_card": "123456",
        "names": "Leo",
        "surnames": "González",
        "phone": "43252525",
        "email": "leo@udea.edu.co",
        "username": "leo",
        "is_active": True,
        "role": "assistant",
        "password": "leo",
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


def test_bad_create_carrier(test_app_with_db):
    data = DATA.copy()
    data.pop("identity_card")
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 422
    response = response.json()
    assert response["detail"][0]["msg"] == "field required"
    assert response["detail"][0]["type"] == "value_error.missing"


def test_auth(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/auth/daniel")

    assert response.status_code == 200
    response = response.json()
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert response["password"] == DATA["password"]


def test_not_auth(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/auth/dani")

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No employee found"


def test_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/1040050021")

    assert response.status_code == 200
    response = response.json()
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "created_at" in response
    assert "last_modified" in response
    assert "password" not in response


def test_not_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/1040")

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No employee found"


def test_get_by_username(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/username/daniel")

    assert response.status_code == 200
    response = response.json()
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "created_at" in response
    assert "last_modified" in response
    assert "password" not in response


def test_not_get_by_username(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/username/dani")

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No employee found"


def test_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 2
    response = response[0]
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "created_at" in response
    assert "last_modified" in response
    assert "password" not in response


def test_get_all_with_filter(test_app_with_db):
    params = {"role": "manager"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 1
    response = response[0]
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "created_at" in response
    assert "last_modified" in response
    assert "password" not in response


def test_not_get_all_with_filter(test_app_with_db):
    params = {"role": "engineer"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_update(test_app_with_db):
    update_data = {"email": "daniel@guane.com.co"}
    response = test_app_with_db.put(
        f"{PREFIX}/1040050021", data=json.dumps(update_data)
    )

    assert response.status_code == 200
    response = response.json()
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == update_data["email"]
    DATA["email"] = update_data["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "created_at" in response
    assert "last_modified" in response
    assert "password" not in response


def test_empty_update(test_app_with_db):
    update_data = {}
    response = test_app_with_db.put(
        f"{PREFIX}/1040050021", data=json.dumps(update_data)
    )

    assert response.status_code == 200
    response = response.json()
    assert response["identity_card"] == DATA["identity_card"]
    assert response["names"] == DATA["names"]
    assert response["surnames"] == DATA["surnames"]
    assert response["phone"] == DATA["phone"]
    assert response["email"] == DATA["email"]
    assert response["username"] == DATA["username"]
    assert response["is_active"] == DATA["is_active"]
    assert response["role"] == DATA["role"]
    assert "created_at" in response
    assert "last_modified" in response
    assert "password" not in response


def test_not_update(test_app_with_db):
    update_data = {"email": "daniel.santar@udea.edu.co"}
    response = test_app_with_db.put(f"{PREFIX}/1040", data=json.dumps(update_data))

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No employee found"


def test_bad_update(test_app_with_db):
    # Test enum and email validations
    update_data = {"email": "daniel@", "role": "engineer"}
    response = test_app_with_db.put(
        f"{PREFIX}/1040050021", data=json.dumps(update_data)
    )

    assert response.status_code == 422
    response = response.json()

    # Email error
    assert response["detail"][0]["msg"] == "value is not a valid email address"
    assert response["detail"][0]["type"] == "value_error.email"

    # Enum error
    assert (
        response["detail"][1]["msg"]
        == "value is not a valid enumeration member; permitted: 'manager', 'assistant', 'supervisor', 'technician'"
    )
    assert response["detail"][1]["type"] == "type_error.enum"


def test_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/123456")

    assert response.status_code == 204


def test_not_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/123456")

    assert response.status_code == 404
