from django.shortcuts import render

from skills import facade


def description(request):
    list_skill_types = facade.list_skill_and_skilltype()
    context = {
        'list_skill_types': list_skill_types,
    }
    return render(request, 'skills/description.html', context)
