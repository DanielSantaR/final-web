def test_ping(test_app):
    response = test_app.get("/api/status")
    assert response.status_code == 200
    assert response.json() == {
        "title": "gazelle-br-cft",
        "description": "This is a microservice to evaluate the CFT business rules",
        "version": "0.0.1",
        "status": "OK",
        "expire_time": 3600,
    }
