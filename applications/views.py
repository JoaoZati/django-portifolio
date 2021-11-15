from django.shortcuts import render


def description(request, slug):
    context = {}
    return render(request, 'applications/description.html', context)


def project(request, slug):
    context = {}
    return render(request, 'applications/project.html', context)
