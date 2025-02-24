def test_items(app, client):
    response = client.get("/items/12345?q=somequery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 12345, "q": "somequery"}