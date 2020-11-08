import json

PREFIX = "/api/vehicles-x-owners"

DATA = {
    "vehicle_id": "MIL712",
    "owner_id": "1040050021",
}


def test_not_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_create(test_app_with_db):
    # First record
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(DATA))

    assert response.status_code == 201
    response = response.json()
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["owner_id"] == DATA["owner_id"]
    assert "created_at" in response
    assert "last_modified" in response

    # Second record
    data = {
        "vehicle_id": "FBI214",
        "owner_id": "9876",
    }
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data))

    assert response.status_code == 201
    response = response.json()
    assert response["vehicle_id"] == data["vehicle_id"]
    assert response["owner_id"] == data["owner_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_bad_create(test_app_with_db):
    data = DATA.copy()
    data.pop("vehicle_id")
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 422
    response = response.json()
    assert response["detail"][0]["msg"] == "field required"
    assert response["detail"][0]["type"] == "value_error.missing"


def test_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/1")

    assert response.status_code == 200
    response = response.json()
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["owner_id"] == DATA["owner_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/3")

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No vehicle_x_owner found"


def test_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 2
    response = response[0]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["owner_id"] == DATA["owner_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_get_all_with_filter(test_app_with_db):
    params = {"owner_id": "1040050021"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 1
    response = response[0]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["owner_id"] == DATA["owner_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_get_all_with_filter(test_app_with_db):
    params = {"vehicle_id": "712"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_update(test_app_with_db):
    update_data = {"owner_id": "9876"}
    response = test_app_with_db.put(f"{PREFIX}/1", data=json.dumps(update_data))

    assert response.status_code == 200
    response = response.json()

    assert response["owner_id"] == update_data["owner_id"]
    DATA["owner_id"] = update_data["owner_id"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_empty_update(test_app_with_db):
    update_data = {}
    response = test_app_with_db.put(f"{PREFIX}/1", data=json.dumps(update_data))

    assert response.status_code == 200
    response = response.json()
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["owner_id"] == DATA["owner_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_update(test_app_with_db):
    update_data = {"owner_id": "1040050021"}
    response = test_app_with_db.put(f"{PREFIX}/3", data=json.dumps(update_data))

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No vehicle_x_owner found"


def test_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/2")

    assert response.status_code == 204


def test_not_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/2")

    assert response.status_code == 404
