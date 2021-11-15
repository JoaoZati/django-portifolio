import pytest
from model_mommy import mommy

from skills import facade
from skills.models import SkillType, Skill


@pytest.fixture
def skill_types(db):
    return [mommy.make(SkillType, title=s) for s in 'title1 title3 title2'.split()]


@pytest.fixture
def skill_types_ordered(db):
    return [mommy.make(SkillType, title=s) for s in 'title3 title2 title1'.split()]


@pytest.fixture
def skills(skill_types):
    list_skill = []
    for type in skill_types:
        list_skill.extend(mommy.make(Skill, 3, type=type))
    return list_skill


@pytest.fixture
def skills_ordered(skill_types_ordered):
    list_skill = []
    for type in skill_types_ordered:
        mommys = mommy.make(Skill, 3, type=type)
        sorted_mommys = sorted(mommys, key=lambda mommy: mommy.title)
        list_skill.extend(sorted_mommys)
    return list_skill


def test_list_skilltype(skill_types):
    assert_list = list(sorted(skill_types, key=lambda skill_type: skill_type.title))
    facade_list = facade.list_skilltype()
    assert assert_list == facade_list


def test_list_skill_ordered(skills_ordered):
    list_final = facade.list_skill_and_skilltype()
    list_assert = []
    for query in list_final:
        list_assert.extend([skill for skill in query.skills])
    assert_list = list(skills_ordered)
    assert list_assert == assert_list


def test_list_skill_not_ordered(skills):
    list_final = facade.list_skill_and_skilltype()
    list_assert = []
    for query in list_final:
        list_assert.extend([skill for skill in query.skills])
    assert_list = list(skills)
    assert not (list_assert == assert_list)
