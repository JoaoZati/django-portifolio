import pytest
from model_mommy import mommy

from skills import facade
from skills.models import SkillType


@pytest.fixture
def skill_types(db):
    return [mommy.make(SkillType, title=s) for s in 'title1 title3 title2'.split()]


def test_list_skill_type(skill_types):
    assert_list = list(sorted(skill_types, key=lambda skill_type: skill_type.title))
    facade_list = facade.list_skill_type()
    assert assert_list == facade_list
