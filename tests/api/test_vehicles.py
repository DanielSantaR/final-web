import json

PREFIX = "/api/vehicles"

DATA = {
    "plate": "MIL712",
    "brand": "renault",
    "model": "2010",
    "color": "gray",
    "vehicle_type": "pick up",
    "state": "received",
    "creation_employee_id": "1040050021",
    "update_employee_id": "1040050021",
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
    assert response["plate"] == DATA["plate"]
    assert response["brand"] == DATA["brand"]
    assert response["model"] == DATA["model"]
    assert response["color"] == DATA["color"]
    assert response["vehicle_type"] == DATA["vehicle_type"]
    assert response["state"] == DATA["state"]
    assert response["creation_employee_id"] == DATA["creation_employee_id"]
    assert response["update_employee_id"] == DATA["update_employee_id"]

    # Second record
    data = {
        "plate": "AUT112",
        "brand": "mazda",
        "model": "2015",
        "color": "white",
        "vehicle_type": "van",
        "state": "received",
        "creation_employee_id": "1040050021",
        "update_employee_id": "1040050021",
    }
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 201
    response = response.json()
    assert response["plate"] == data["plate"]
    assert response["brand"] == data["brand"]
    assert response["model"] == data["model"]
    assert response["color"] == data["color"]
    assert response["vehicle_type"] == data["vehicle_type"]
    assert response["state"] == data["state"]
    assert response["creation_employee_id"] == data["creation_employee_id"]
    assert response["update_employee_id"] == data["update_employee_id"]


def test_bad_create_carrier(test_app_with_db):
    data = DATA.copy()
    data.pop("plate")
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 422
    response = response.json()
    assert response["detail"][0]["msg"] == "field required"
    assert response["detail"][0]["type"] == "value_error.missing"


def test_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/MIL712")

    assert response.status_code == 200
    response = response.json()
    assert response["plate"] == DATA["plate"]
    assert response["brand"] == DATA["brand"]
    assert response["model"] == DATA["model"]
    assert response["color"] == DATA["color"]
    assert response["vehicle_type"] == DATA["vehicle_type"]
    assert response["state"] == DATA["state"]
    assert response["creation_employee_id"] == DATA["creation_employee_id"]
    assert response["update_employee_id"] == DATA["update_employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/712")

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No vehicle found"


def test_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 2
    response = response[0]
    assert response["plate"] == DATA["plate"]
    assert response["brand"] == DATA["brand"]
    assert response["model"] == DATA["model"]
    assert response["color"] == DATA["color"]
    assert response["vehicle_type"] == DATA["vehicle_type"]
    assert response["state"] == DATA["state"]
    assert response["creation_employee_id"] == DATA["creation_employee_id"]
    assert response["update_employee_id"] == DATA["update_employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_get_all_with_filter(test_app_with_db):
    params = {"brand": "renault"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 1
    response = response[0]
    assert response["plate"] == DATA["plate"]
    assert response["brand"] == DATA["brand"]
    assert response["model"] == DATA["model"]
    assert response["color"] == DATA["color"]
    assert response["vehicle_type"] == DATA["vehicle_type"]
    assert response["state"] == DATA["state"]
    assert response["creation_employee_id"] == DATA["creation_employee_id"]
    assert response["update_employee_id"] == DATA["update_employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_get_all_with_filter(test_app_with_db):
    params = {"model": "2000"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_update(test_app_with_db):
    update_data = {"model": "2012"}
    response = test_app_with_db.put(f"{PREFIX}/MIL712", data=json.dumps(update_data))

    assert response.status_code == 200
    response = response.json()
    assert response["plate"] == DATA["plate"]
    assert response["brand"] == DATA["brand"]
    assert response["model"] == update_data["model"]
    DATA["model"] = update_data["model"]
    assert response["color"] == DATA["color"]
    assert response["vehicle_type"] == DATA["vehicle_type"]
    assert response["state"] == DATA["state"]
    assert response["creation_employee_id"] == DATA["creation_employee_id"]
    assert response["update_employee_id"] == DATA["update_employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_empty_update(test_app_with_db):
    update_data = {}
    response = test_app_with_db.put(f"{PREFIX}/MIL712", data=json.dumps(update_data))

    assert response.status_code == 200
    response = response.json()
    assert response["plate"] == DATA["plate"]
    assert response["brand"] == DATA["brand"]
    assert response["model"] == DATA["model"]
    assert response["color"] == DATA["color"]
    assert response["vehicle_type"] == DATA["vehicle_type"]
    assert response["state"] == DATA["state"]
    assert response["creation_employee_id"] == DATA["creation_employee_id"]
    assert response["update_employee_id"] == DATA["update_employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_update(test_app_with_db):
    update_data = {"color": "black"}
    response = test_app_with_db.put(f"{PREFIX}/712", data=json.dumps(update_data))

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No vehicle found"


def test_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/AUT112")

    assert response.status_code == 204


def test_not_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/AUT112")

    assert response.status_code == 404
