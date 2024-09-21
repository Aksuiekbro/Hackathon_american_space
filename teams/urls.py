from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.index_search, name="search"),
    path("teams/", views.teams, name="teams"),
]