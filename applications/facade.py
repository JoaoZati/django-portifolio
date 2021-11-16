from applications.models import Application, ApplicationType
from django.db.models import Prefetch


def list_applicationtype():
    ordered_application = Application.objects.order_by('order')
    return list(
        ApplicationType.objects.order_by('order').prefetch_related(
            Prefetch('application_set', queryset=ordered_application, to_attr='applications')
        ).all()
    )
