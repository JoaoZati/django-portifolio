from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from applications.models import Application, ApplicationType


@admin.register(ApplicationType)
class ApplicationTypeAdmin(OrderedModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'online_app',
        'img',
        'move_up_down_links',
    )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Application)
class ApplicationAdmin(OrderedModelAdmin):
    list_display = (
        'title',
        'content',
        'slug',
        'link_github',
        'link_site',
        'application_type',
        'move_up_down_links',
    )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('application_type',)
    ordering = ('application_type', 'title')
