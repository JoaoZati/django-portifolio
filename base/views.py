from django.shortcuts import render
from skills import facade as sk_facade
from applications import facade as app_facade
from frontapps import facade as fapp_facade


def home(request):
    list_skill_types = sk_facade.list_skill_and_skilltype()
    list_application_dropdown = app_facade.list_applicationtype()
    list_front_apps = fapp_facade.list_front_apps()
    context = {
        'list_skill_types': list_skill_types,
        'list_application_dropdown': list_application_dropdown,
        'list_front_apps': list_front_apps,
    }
    return render(request, 'base/home.html', context)
