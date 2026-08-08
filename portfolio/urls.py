from django.urls import path

from . import views


app_name = "portfolio"


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "a-propos/",
        views.about,
        name="about",
    ),

    path(
        "services/",
        views.services,
        name="services",
    ),

    path(
        "projets/",
        views.projects,
        name="projects",
    ),

    path(
        "projets/<slug:slug>/",
        views.project_detail,
        name="project_detail",
    ),

    path(
        "contact/",
        views.contact,
        name="contact",
    ),
]