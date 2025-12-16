from django.urls import path
from cookie import views

urlpatterns = [
    path("set/", views.set),
    path("get/", views.get),
    path("delete/", views.delete),
    path("update/", views.update),
]
