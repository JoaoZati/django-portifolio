from django.shortcuts import render


def description(request):
    context = {}
    return render(request, 'skills/description.html', context)
