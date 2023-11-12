from pathlib import Path
import json


def test_logger(testdir: Path, caplog, client):
    response = client.get('/hello/', headers={'X-Test-Header': 'FOO'})
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hello world!'}

    logs_path = testdir/'microblog-api.log'
    assert logs_path.exists()

    log = json.load(logs_path)
    assert log['@timestamp']
    assert log['log.level'] == 'info'
    assert log['message'] == \
        'Request from testclient:50000 to http://testserver/hello/ handled'

    request = log.get('request')
    assert request
    assert request['client']['host'] == 'testclient'
    assert request['client']['port'] == 50000
    assert request['headers']['x-test-header'] == 'FOO'
    assert request['method'] == 'GET'
    assert request['url'] == 'http://testserver/hello/'

    response = log.get('response')
    assert response
    assert response['charset'] == 'utf-8'
    assert response['media_type'] == 'application/json'
    assert response['status_code'] == 200
    parsed_body = json.loads(response['body'][2:-1].encode())
    assert parsed_body == {'msg': 'Hello world!'}
