import pytest
from model_mommy import mommy

from main.django_assertions import assert_contains
from skills.models import SkillType, Skill
from django.urls import reverse

from django.core.files.uploadedfile import SimpleUploadedFile


small_gif = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


@pytest.fixture
def skill_types(db):
    return [mommy.make(
        SkillType,
        title=s,
        static_image=SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
    ) for s in 'title1 title3 title2'.split()]


@pytest.fixture
def skills(skill_types):
    list_skill = []
    for type in skill_types:
        list_skill.extend(mommy.make(Skill, 3, type=type))
    return list_skill


@pytest.fixture
def resp(client, skill_types, skills):
    resp = client.get(reverse('base:home'))
    return resp


def test_skilltypes_titles_home(resp, skill_types):
    for skill_type in skill_types:
        assert_contains(resp, skill_type.title)


def test_skills_titles_home(resp, skills):
    for skill in skills:
        assert_contains(resp, skill.title)
