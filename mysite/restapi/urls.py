from django.urls import path

from . import views

urlpatterns = [
    path('', views.restapi_main, name='restapi'),
]