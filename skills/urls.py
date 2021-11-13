from django.urls import path

from skills.views import description

app_name = 'skills'
urlpatterns = [
    path('', description, name='description'),
]
