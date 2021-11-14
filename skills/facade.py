from skills.models import Skill, SkillType


def list_skill_type():
    return list(SkillType.objects.order_by('title'))
