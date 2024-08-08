from testrepo.app import load


def test_health_route():
    app = load()
    test_client = app.test_client()
    response = test_client.get("/")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == {
        "status": "pass",
        "message": "flux capacitor is fluxing",
        "version": "0.0.0"
    }
