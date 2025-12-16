from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("thank-you/", views.thank),
    path("all-data/", views.allData),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
