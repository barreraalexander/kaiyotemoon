import pytest
from server import schemas

def test_get_all_posts(client):
    res = client.get('/poems/')
    assert res.status_code == 200


def test_get_one_post(client):
    res = client.get('/poems/1')
    assert res.status_code == 200

def test_get_one_post_failure(client):
    res = client.get('/poems/999')
    assert res.status_code == 404

@pytest.mark.parametrize("poem_index, status_code", [
    (0, 200),
    (10, 200),
    (20, 200),
    (100, 404),
    (200, 404),
])
def test_get_many(client, poem_index, status_code):
    res = client.get(f'/poems/{poem_index}')
    assert res.status_code == status_code

