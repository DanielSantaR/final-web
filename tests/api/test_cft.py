import json

PREFIX = "/api/cft/"


def test_create_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_create_default_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}", data=json.dumps({"broker_id": 1, "contract_id": 1}),
    )

    assert response.status_code == 201
    response = response.json()
    assert type(response["id"]) == int

    broker_id = response["broker_id"]
    contract_id = response["contract_id"]
    lower_limit = response["lower_limit"]
    upper_limit = response["upper_limit"]
    fee = response["fee"]

    assert lower_limit[0] == 1
    assert upper_limit[0] == 1
    assert fee[0] == 0

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_faile_creating_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    try:
        fail_response = test_app_with_db.post(
            f"{PREFIX}",
            data=json.dumps(
                {
                    "broker_id": 1,
                    "contract_id": 1,
                    "lower_limit": [10, 100, 200],
                    "upper_limit": [100, 200, 700],
                    "fee": [50, 100, 150],
                    "is_active": True,
                }
            ),
        )
        print(fail_response)
    except Exception as e:
        print(e)

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_bad_request_create_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 400
    response = response.json()["detail"]
    assert response == "Check that lower limit, upper limit and fees are the same size"


def test_get_carriers(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"{PREFIX}")

    assert response.status_code == 200

    response_list = response.json()

    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1

    broker_id = response_list[0]["broker_id"]
    contract_id = response_list[0]["contract_id"]

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_get_no_carriers(test_app_with_db):

    response = test_app_with_db.get(f"{PREFIX}")
    assert response.status_code == 404

    response = response.json()

    assert response["detail"] == "No carriers found"


def test_get_byid(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    summary_id = response.json()["id"]
    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]
    lower_limit = response.json()["lower_limit"]
    upper_limit = response.json()["upper_limit"]
    fee = response.json()["fee"]
    is_active = response.json()["is_active"]

    response = test_app_with_db.get(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")
    assert response.status_code == 200

    response_list = response.json()
    assert response_list["id"] == summary_id
    assert response_list["broker_id"] == broker_id
    assert response_list["contract_id"] == contract_id
    assert response_list["lower_limit"] == lower_limit
    assert response_list["upper_limit"] == upper_limit
    assert response_list["fee"] == fee
    assert response_list["is_active"] == is_active

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_fail_get_byid(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    response = test_app_with_db.get(f"{PREFIX}{str(broker_id)}/{str(contract_id + 1)}")
    assert response.status_code == 404

    response = response.json()
    assert response["detail"] == "No carrier found"

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_delete_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")
    assert response.status_code == 204

    response = response.json()
    assert response == 1


def test_fail_delete_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    response = test_app_with_db.delete(
        f"{PREFIX}{str(broker_id)}/{str(contract_id + 1)}"
    )

    assert response.status_code == 404

    response = response.json()
    assert response == 0

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_update_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    update_payload = {
        "lower_limit": [10, 100, 200, 700],
        "upper_limit": [100, 200, 700, 1000],
        "fee": [50, 100, 150, 200],
        "is_active": True,
    }

    response_update = test_app_with_db.put(
        f"{PREFIX}{str(broker_id)}/{str(contract_id)}", data=json.dumps(update_payload),
    )

    response = test_app_with_db.get(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")
    assert response.status_code == 200

    response_list = response.json()
    assert response_list["lower_limit"] == response_update.json()["lower_limit"]
    assert len(response_list["lower_limit"]) == len(
        response_update.json()["lower_limit"]
    )
    assert response_list["upper_limit"] == response_update.json()["upper_limit"]
    assert len(response_list["upper_limit"]) == len(
        response_update.json()["upper_limit"]
    )
    assert response_list["fee"] == response_update.json()["fee"]
    assert len(response_list["fee"]) == len(response_update.json()["fee"])
    assert response_list["is_active"] == response_update.json()["is_active"]

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_fail_update_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    update_payload = {
        "lower_limit": [10, 100, 200, 700],
        "upper_limit": [100, 200, 700, 1000],
        "fee": [50, 100, 150, 200],
        "is_active": True,
    }

    response_update = test_app_with_db.put(
        f"{PREFIX}{str(broker_id)}/{str(contract_id + 1)}",
        data=json.dumps(update_payload),
    )

    assert response_update.status_code == 404

    response = response_update.json()
    assert response["detail"] == "No carrier found"

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_bad_request_update_carrier(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    summary_id = response.json()["id"]
    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]
    lower_limit = response.json()["lower_limit"]
    upper_limit = response.json()["upper_limit"]
    fee = response.json()["fee"]
    is_active = response.json()["is_active"]

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    update_payload = {
        "lower_limit": [10, 100],
        "upper_limit": [100, 200, 800],
        "is_active": False,
    }

    response = test_app_with_db.put(
        f"{PREFIX}{str(broker_id)}/{str(contract_id)}", data=json.dumps(update_payload),
    )

    assert response.status_code == 400
    response = response.json()["detail"]
    assert response == "Check that lower limit, upper limit and fees are the same size"

    response = test_app_with_db.get(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    response = response.json()
    assert response["id"] == summary_id
    assert response["broker_id"] == broker_id
    assert response["contract_id"] == contract_id
    assert response["lower_limit"] == lower_limit
    assert response["upper_limit"] == upper_limit
    assert response["fee"] == fee
    assert response["is_active"] == is_active

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_get_carrier_fee(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]
    fee = response.json()["fee"][0]

    response = test_app_with_db.get(
        f"{PREFIX}get_fees/{str(broker_id)}/{str(contract_id)}"
    )
    assert response.status_code == 200

    response_list = response.json()
    assert response_list["broker_id"] == broker_id
    assert response_list["contract_id"] == contract_id
    assert response_list["fee"] == fee

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_get_fail_carrier_fee(test_app_with_db):
    response = test_app_with_db.post(
        f"{PREFIX}",
        data=json.dumps(
            {
                "broker_id": 1,
                "contract_id": 1,
                "lower_limit": [10, 100, 200],
                "upper_limit": [100, 200, 700],
                "fee": [50, 100, 150],
                "is_active": True,
            }
        ),
    )

    assert response.status_code == 201
    assert type(response.json()["id"]) == int

    broker_id = response.json()["broker_id"]
    contract_id = response.json()["contract_id"]

    response = test_app_with_db.get(
        f"{PREFIX}get_fees/{str(broker_id)}/{str(contract_id + 1)}"
    )
    assert response.status_code == 404

    response = response.json()
    assert response["detail"] == "No carrier found"

    response = test_app_with_db.delete(f"{PREFIX}{str(broker_id)}/{str(contract_id)}")

    assert response.status_code == 204


def test_count(test_app_with_db):
    brokers = [1, 2]
    carriers = [1, 2, 3, 4, 5, 6, 7, 8]
    lower_limits = [[10], [20], [500], [10], [100], [30], [450], [100]]
    upper_limits = [[500], [200], [800], [900], [1000], [300], [700], [600]]
    fees = [[10], [20], [30], [10], [20], [30], [40], [40]]
    actives = [True, True, True, False, False, True, True, True]

    for broker in brokers:
        for i, carrier in enumerate(carriers):
            response = test_app_with_db.post(
                f"{PREFIX}",
                data=json.dumps(
                    {
                        "broker_id": broker,
                        "contract_id": carrier,
                        "lower_limit": lower_limits[i],
                        "upper_limit": upper_limits[i],
                        "fee": fees[i],
                        "is_active": actives[i],
                    }
                ),
            )
            assert response.status_code == 201
            assert type(response.json()["id"]) == int

    response = test_app_with_db.post(
        f"{PREFIX}count/", data=json.dumps({"broker_id": 1})
    )
    assert response.status_code == 200
    response = response.json()
    assert response == 8

    response = test_app_with_db.post(
        f"{PREFIX}count/", data=json.dumps({"broker_id": 1, "is_active": True})
    )
    assert response.status_code == 200
    response = response.json()
    assert response == 6

    response = test_app_with_db.post(
        f"{PREFIX}count/", data=json.dumps({"contract_id": 1})
    )
    assert response.status_code == 200
    response = response.json()
    assert response == 2

    for broker_id in brokers:
        for contract_id in carriers:
            response = test_app_with_db.delete(
                f"{PREFIX}{str(broker_id)}/{str(contract_id)}"
            )

            assert response.status_code == 204


def test_check_carriers(test_app_with_db):

    brokers = [1, 2]
    carriers = [1, 2, 3, 4, 5, 6, 7, 8]
    lower_limits = [[10, 400], [20], [500], [10], [100], [30], [450], [100]]
    upper_limits = [
        [400, 600],
        [200],
        [800],
        [900],
        [1000],
        [300],
        [700],
        [600],
    ]
    fees = [[10, 20], [20], [30], [10], [20], [30], [40], [40]]
    actives = [True, True, True, False, False, True, True, True]

    for broker in brokers:
        for i, carrier in enumerate(carriers):
            response = test_app_with_db.post(
                f"{PREFIX}",
                data=json.dumps(
                    {
                        "broker_id": broker,
                        "contract_id": carrier,
                        "lower_limit": lower_limits[i],
                        "upper_limit": upper_limits[i],
                        "fee": fees[i],
                        "is_active": actives[i],
                    }
                ),
            )
            assert response.status_code == 201
            assert type(response.json()["id"]) == int

    restriction = "400 cft"
    broker = 1
    response = test_app_with_db.post(
        f"{PREFIX}check_carriers/",
        data=json.dumps(
            {"restriction": restriction, "broker_id": broker, "carriers_id": carriers}
        ),
    )

    assert response.status_code == 200
    response = response.json()
    assert response["available_carriers"] == [
        {"broker_id": 1, "contract_id": 1, "fee": 20},
        {"broker_id": 1, "contract_id": 8, "fee": 40},
        {"broker_id": 1, "contract_id": 4, "fee": 0},
        {"broker_id": 1, "contract_id": 5, "fee": 0},
    ]
    assert response["exclude_lower_carriers"] == [
        {
            "broker_id": 1,
            "contract_id": 3,
            "message": "CFT smaller than the lower limit",
        },
        {
            "broker_id": 1,
            "contract_id": 7,
            "message": "CFT smaller than the lower limit",
        },
    ]
    assert response["exclude_upper_carriers"] == [
        {
            "broker_id": 1,
            "contract_id": 2,
            "message": "CFT bigger than the upper limit",
        },
        {
            "broker_id": 1,
            "contract_id": 6,
            "message": "CFT bigger than the upper limit",
        },
    ]

    for broker_id in brokers:
        for contract_id in carriers:
            response = test_app_with_db.delete(
                f"{PREFIX}{str(broker_id)}/{str(contract_id)}"
            )

            assert response.status_code == 204
