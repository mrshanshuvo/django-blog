from django.urls import path
from sessiontut import views

urlpatterns = [
    path("set/", views.set),
    path("get/", views.get),
    path("delete/", views.delete),
]
