def test_ping(test_app):
    response = test_app.get("/api/status")
    assert response.status_code == 200
    assert response.json() == {
        "title": "taller",
        "description": "This is a microservice to ing web final workshop",
        "version": "0.0.1",
        "status": "OK",
    }
