def test_get_hello(client):
    response = client.get('/api/hello/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hello world!'}
