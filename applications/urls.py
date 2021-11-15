from django.urls import path

from applications.views import description


app_name = 'applications'
urlpatterns = [
    path('', description, name='description'),
]
