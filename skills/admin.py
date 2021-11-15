from django.contrib import admin

from skills.models import SkillType, Skill


@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'static_image')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'type')
