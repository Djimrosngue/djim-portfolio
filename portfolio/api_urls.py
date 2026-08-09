from django.urls import path

from .api_views import (
    ContactCreateAPIView,
    EducationListAPIView,
    ProfileAPIView,
    ProjectDetailAPIView,
    ProjectListAPIView,
    ServiceListAPIView,
    SkillListAPIView,
)


urlpatterns = [

    path("profile/",
        ProfileAPIView.as_view(),
        name="api-profile",
    ),

    path("skills/",
        SkillListAPIView.as_view(),
        name="api-skills",
    ),

    path("services/",
        ServiceListAPIView.as_view(),
        name="api-services",
    ),

    path("projects/",
        ProjectListAPIView.as_view(),
        name="api-projects",
    ),

    path("projects/<slug:slug>/",
        ProjectDetailAPIView.as_view(),
        name="api-project-detail",
    ),

    path("education/",
        EducationListAPIView.as_view(),
        name="api-education",
    ),

    path("contact/",
        ContactCreateAPIView.as_view(),
        name="api-contact",
    ),
]