from django.shortcuts import render

from applications import facade


def description(request, slug):
    application_type = facade.find_application_type(slug)
    applications = facade.find_application_from_type(application_type)
    context = {
        'application_type': application_type,
        'applications': applications,
    }
    return render(request, 'applications/description.html', context)


def project(request, slug):
    context = {}
    return render(request, 'applications/project.html', context)
