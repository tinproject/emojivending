

def test_metrics_endpoint(client):
    response = client.get("/metrics")

    assert 200 == response.status_code
    assert "text/plain; version=0.0.4; charset=utf-8" == response.content_type
