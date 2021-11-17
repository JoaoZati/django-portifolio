import pytest
from django.urls import reverse

from main.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_carousel(resp):
    assert_contains(resp, '<div id="carouselExampleIndicators" '
                          'class="carousel carousel-dark slide" data-bs-ride="carousel">')


def test_featurette(resp):
    assert_contains(resp, '<h2 class="featurette-heading">Projeto Django Devpro.')
