import json

def test_helloworld(client):
    res = client.get('/api/v1.0/hello/test')

    assert res.status_code == 200
    print(dir(res))
    assert json.loads(res.get_data(as_text=True)) == {"hello": "test"}
