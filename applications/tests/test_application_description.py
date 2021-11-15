import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('applications:description'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
