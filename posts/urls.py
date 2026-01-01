from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post"),
    path("tags/<int:id>", views.tags, name="tags"),
    path("search/", views.SearchView.as_view(), name="search"),
]
