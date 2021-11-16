from applications.models import Application, ApplicationType
from django.db.models import Prefetch


def list_applicationtype():
    ordered_application = Application.objects.order_by('order')
    return list(
        ApplicationType.objects.order_by('order').prefetch_related(
            Prefetch('application_set', queryset=ordered_application, to_attr='applications')
        ).all()
    )


def find_application_type(slug):
    return ApplicationType.objects.get(slug=slug)


def find_application_from_type(application_type):
    return list(application_type.application_set.order_by('order').all())
