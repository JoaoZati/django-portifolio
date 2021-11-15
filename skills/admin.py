from django.contrib import admin

from skills.models import SkillType, Skill


@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'type')
