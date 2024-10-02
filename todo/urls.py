from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("add", views.Add, name="add"),
    path("<int:todo_id>/delete", views.Delete, name="delete"),
    path("<int:todo_id>/update", views.Update, name="update"),

]