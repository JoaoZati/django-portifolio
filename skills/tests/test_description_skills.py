import pytest
from django.urls import reverse
from main.django_assertions import assert_contains

from model_mommy import mommy
from skills.models import SkillType, Skill


@pytest.fixture
def skill_types(db):
    return [mommy.make(SkillType, title=s) for s in 'title1 title2 title3'.split()]


@pytest.fixture
def skills(skill_types):
    list_skill = []
    for type in skill_types:
        list_skill.extend(mommy.make(Skill, 3, type=type))
    return list_skill


@pytest.fixture
def resp(client, skill_types, skills):
    resp = client.get(reverse('skills:description'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_skilltypes_titles(resp, skill_types):
    for skill_type in skill_types:
        assert_contains(resp, skill_type.title)


def test_skills_titles(resp, skills):
    for skill in skills:
        assert_contains(resp, skill.title)


def test_skills_content(resp, skills):
    for skill in skills:
        assert_contains(resp, skill.content)
