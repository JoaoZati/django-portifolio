from frontapps.models import FrontApp


def list_front_apps():
    return FrontApp.objects.all()
