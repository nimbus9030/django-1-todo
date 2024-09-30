from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("add", views.Add, name="add"),
]