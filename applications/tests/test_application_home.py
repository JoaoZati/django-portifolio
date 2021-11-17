import pytest
from django.urls import reverse
from main.django_assertions import assert_contains

from model_mommy import mommy
from applications.models import ApplicationType, Application
from django.core.files.uploadedfile import SimpleUploadedFile

small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


@pytest.fixture
def application_types(db):
    return mommy.make(
        ApplicationType,
        2,
        img=SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
    )


@pytest.fixture
def applications(application_types):
    list_applications = []
    for application_type in application_types:
        list_applications.extend(mommy.make(Application, 3, application_type=application_type))
    return list_applications


@pytest.fixture
def resp(client, application_types, applications):
    resp = client.get(reverse('base:home'))
    return resp


def test_home_status_code(resp):
    assert resp.status_code == 200


def test_applications_type_title(resp, application_types):
    for app in application_types:
        assert_contains(resp, app.title)


def test_applications_type_description(resp, application_types):
    for app in application_types:
        assert_contains(resp, app.description)


def test_applications_type_url(resp, application_types):
    for app in application_types:
        assert_contains(resp, app.get_absolute_url())


def test_applications_type_image(resp, application_types):
    for app in application_types:
        assert_contains(resp, app.img.url)


def test_applications_type_navbar_title(resp, application_types):
    for app in application_types:
        assert_contains(resp, f'{app.title}\n')


def test_applications_navbar_title(resp, applications):
    for app in applications:
        assert_contains(resp, f'>{app.title}</a>')


def test_applications_navbar_url(resp, applications):
    for app in applications:
        assert_contains(resp, f'<li><a class="dropdown-item" href="{app.get_absolute_url()}">')
