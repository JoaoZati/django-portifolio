from applications import facade


def list_application_types(request):
    return {'APPLICATION_TYPES': facade.list_applicationtype()}
