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
def application(application_type):
    return mommy.make(Application, application_type=application_type)


@pytest.fixture
def resp(client, application_type, application):
    resp = client.get(reverse('applications:project', kwargs={'slug': application.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_application_title(resp, application):
    assert_contains(resp, f'<h2>{application.title}</h2')


def test_application_url_father(resp, application, application_type):
    assert_contains(resp, f'<h4>Categoria: <a href="{application_type.get_absolute_url()}"')


def test_application_content(resp, application):
    assert_contains(resp, application.content)


def test_application_link_site(resp, application):
    assert_contains(resp, application.link_site)


def test_application_link_github(resp, application):
    assert_contains(resp, application.link_github)
