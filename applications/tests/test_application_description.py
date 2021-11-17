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
def application_type(db):
    return mommy.make(
        ApplicationType,
        img=SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
    )


@pytest.fixture
def applications(application_type):
    return mommy.make(Application, 3, application_type=application_type)


@pytest.fixture
def resp(client, application_type, applications):
    resp = client.get(reverse('applications:description', kwargs={'slug': application_type.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_application_type_title(resp, application_type):
    assert_contains(resp, f'<h2>{application_type.title}</h2>')


def test_application_type_description(resp, application_type):
    assert_contains(resp, application_type.description)


def test_application_type_img(resp, application_type):
    assert_contains(resp, application_type.img.url)


def test_applications_title(resp, applications):
    for app in applications:
        assert_contains(resp, f'<h4>{app.title}</h4>')


def test_applications_content(resp, applications):
    for app in applications:
        assert_contains(resp, app.content)


def test_applications_link_github(resp, applications):
    for app in applications:
        assert_contains(resp, app.link_github)


def test_applications_link_site(resp, applications):
    for app in applications:
        assert_contains(resp, app.link_site)


def test_applications_get_absolute_url(resp, applications):
    for app in applications:
        assert_contains(resp, f'<p><a class="btn btn-dark" href="{app.get_absolute_url()}"')
