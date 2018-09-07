

def test_landing_endpoint(client):
    assert client.get("/").status_code == 200
