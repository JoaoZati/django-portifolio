from django.contrib import admin
from frontapps.models import FrontApp
from ordered_model.admin import OrderedModelAdmin


@admin.register(FrontApp)
class FrontAppAdmin(OrderedModelAdmin):
    list_display = (
        'title',
        'subtitle',
        'content',
        'img',
        'application',
        'move_up_down_links',
    )
