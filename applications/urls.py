from django.urls import path

from applications.views import description, project


app_name = 'applications'
urlpatterns = [
    path('<slug:slug>', description, name='description'),
    path('projects/<slug:slug>', project, name='project'),
]
