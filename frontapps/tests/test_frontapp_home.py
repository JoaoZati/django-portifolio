import pytest
from django.urls import reverse
from main.django_assertions import assert_contains

from model_mommy import mommy
from applications.models import Application, ApplicationType
from frontapps.models import FrontApp
from django.core.files.uploadedfile import SimpleUploadedFile

small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


@pytest.fixture
def application_type(db):
    return mommy.make(
        ApplicationType,
        img=SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
    )


@pytest.fixture
def application(application_type):
    return mommy.make(Application, application_type=application_type)


@pytest.fixture
def front_apps(db):
    return mommy.make(
        FrontApp,
        2,
        img=SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
    )


@pytest.fixture
def resp(client, application_type, application, front_apps):
    resp = client.get(reverse('base:home'))
    return resp


def test_front_apps_title(resp, front_apps):
    for app in front_apps:
        assert_contains(resp, app.title)


def test_front_apps_subtitle(resp, front_apps):
    for app in front_apps:
        assert_contains(resp, app.subtitle)


def test_front_apps_content(resp, front_apps):
    for app in front_apps:
        assert_contains(resp, app.content)


def test_front_apps_img_url(resp, front_apps):
    for app in front_apps:
        assert_contains(resp, app.img.url)


def test_front_apps_application_url(resp, front_apps):
    for app in front_apps:
        assert_contains(resp, app.application.get_absolute_url())
