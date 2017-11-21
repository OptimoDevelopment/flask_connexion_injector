import json

def test_helloworld(client):
    res = client.post('/api/v1.0/fibonacci', data=json.dumps({"index": 5}), content_type='application/json')

    assert res.status_code == 200
    assert json.loads(res.get_data(as_text=True)) == {"index": 5, "value": [0, 1, 1, 2, 3]}
