import pytest
from model_mommy import mommy

from applications import facade
from applications.models import Application, ApplicationType


@pytest.fixture
def application_types(db):
    return [mommy.make(ApplicationType, title=s) for s in 'title1 title2 title3'.split()]


@pytest.fixture
def applications(application_types):
    list_application = []
    for type in application_types:
        mommys = [mommy.make(Application, title=s, application_type=type) for s in 'title1 title2 title3'.split()]
        list_application.extend(mommys)
    return list_application


def test_list_application_and_application_type(applications):
    list_final = facade.list_applicationtype()
    list_assert = []
    for query in list_final:
        list_assert.extend([application for application in query.applications])
    assert len(list_assert) == len(applications)
