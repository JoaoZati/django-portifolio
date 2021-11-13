import pytest
from django.urls import reverse

from main.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('skills:description'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
