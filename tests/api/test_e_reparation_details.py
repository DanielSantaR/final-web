import json

PREFIX = "/api/details"

DATA = {
    "description": "received",
    "cost": 0,
    "spare_parts": [],
    "state": "received",
    "vehicle_id": "MIL712",
    "employee_id": "1040050021",
}


def test_not_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_create(test_app_with_db):
    # First record
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(DATA),)

    assert response.status_code == 201
    response = response.json()
    assert response["description"] == DATA["description"]
    assert response["cost"] == DATA["cost"]
    assert response["spare_parts"] == DATA["spare_parts"]
    assert response["state"] == DATA["state"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["employee_id"] == DATA["employee_id"]

    # Second record
    data = {
        "description": "received",
        "cost": 0,
        "spare_parts": [],
        "state": "received",
        "vehicle_id": "FBI214",
        "employee_id": "1040050021",
    }
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 201
    response = response.json()
    assert response["description"] == data["description"]
    assert response["cost"] == data["cost"]
    assert response["spare_parts"] == data["spare_parts"]
    assert response["state"] == data["state"]
    assert response["vehicle_id"] == data["vehicle_id"]
    assert response["employee_id"] == data["employee_id"]

    # Third record
    data = {
        "description": "the car was painted",
        "cost": 200,
        "spare_parts": ["paint"],
        "state": "ready",
        "vehicle_id": "MIL712",
        "employee_id": "2468",
    }
    response = test_app_with_db.post(f"{PREFIX}", data=json.dumps(data),)

    assert response.status_code == 201
    response = response.json()
    assert response["description"] == data["description"]
    assert response["cost"] == data["cost"]
    assert response["spare_parts"] == data["spare_parts"]
    assert response["state"] == data["state"]
    assert response["vehicle_id"] == data["vehicle_id"]
    assert response["employee_id"] == data["employee_id"]


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
    assert response["description"] == DATA["description"]
    assert response["cost"] == DATA["cost"]
    assert response["spare_parts"] == DATA["spare_parts"]
    assert response["state"] == DATA["state"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["employee_id"] == DATA["employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_get_by_id(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}/5")

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No reparation detail found"


def test_get_all(test_app_with_db):
    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 3
    response = response[0]
    assert response["description"] == DATA["description"]
    assert response["cost"] == DATA["cost"]
    assert response["spare_parts"] == DATA["spare_parts"]
    assert response["state"] == DATA["state"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["employee_id"] == DATA["employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_get_all_with_filter(test_app_with_db):
    params = {"employee_id": "1040050021"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert len(response) == 2
    response = response[0]
    assert response["description"] == DATA["description"]
    assert response["cost"] == DATA["cost"]
    assert response["spare_parts"] == DATA["spare_parts"]
    assert response["state"] == DATA["state"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["employee_id"] == DATA["employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_get_all_with_filter(test_app_with_db):
    params = {"vehicle_id": "AUT214"}
    response = test_app_with_db.get(f"{PREFIX}", params=params)

    assert response.status_code == 200
    response = response.json()
    assert response == []


def test_update(test_app_with_db):
    update_data = {"description": "tires are being changed", "state": "in process"}
    response = test_app_with_db.put(f"{PREFIX}/1", data=json.dumps(update_data))

    assert response.status_code == 200
    response = response.json()
    assert response["description"] == update_data["description"]
    DATA["description"] = update_data["description"]
    assert response["cost"] == DATA["cost"]
    assert response["spare_parts"] == DATA["spare_parts"]
    assert response["state"] == update_data["state"]
    DATA["state"] = update_data["state"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["employee_id"] == DATA["employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_empty_update(test_app_with_db):
    update_data = {}
    response = test_app_with_db.put(f"{PREFIX}/1", data=json.dumps(update_data))

    assert response.status_code == 200
    response = response.json()
    assert response["description"] == DATA["description"]
    assert response["cost"] == DATA["cost"]
    assert response["spare_parts"] == DATA["spare_parts"]
    assert response["state"] == DATA["state"]
    assert response["vehicle_id"] == DATA["vehicle_id"]
    assert response["employee_id"] == DATA["employee_id"]
    assert "created_at" in response
    assert "last_modified" in response


def test_not_update(test_app_with_db):
    update_data = {"description": "tires are being changed", "state": "in process"}
    response = test_app_with_db.put(f"{PREFIX}/5", data=json.dumps(update_data))

    assert response.status_code == 404
    response = response.json()
    assert response["detail"] == "No reparation detail found"


def test_bad_update(test_app_with_db):
    # Test enum and email validations
    update_data = {"spare_parts": "tires"}
    response = test_app_with_db.put(f"{PREFIX}/1", data=json.dumps(update_data))

    assert response.status_code == 422
    response = response.json()

    # Email error
    assert response["detail"][0]["msg"] == "value is not a valid list"
    assert response["detail"][0]["type"] == "type_error.list"


def test_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/2")

    assert response.status_code == 204


def test_not_delete(test_app_with_db):
    response = test_app_with_db.delete(f"{PREFIX}/2")
    assert response.status_code == 404
