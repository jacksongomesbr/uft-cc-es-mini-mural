from django.urls import path

from . import views

urlpatterns = [
    path("", views.mural, name="mural"),
    path("avisos/novo/", views.novo, name="novo"),
    path("avisos/", views.criar, name="criar"),
]
