from skills.models import Skill, SkillType
from django.db.models import Prefetch


def list_skilltype():
    return list(SkillType.objects.order_by('title'))


def list_skill_and_skilltype():
    ordered_skills = Skill.objects.order_by('title')
    return list(SkillType.objects.order_by('title').prefetch_related(
        Prefetch('skill_set', queryset=ordered_skills, to_attr='skills')
    ).all())

