from rest_framework import generics

from .models import (
    ContactMessage,
    Education,
    Profile,
    Project,
    Service,
    Skill,
)

from .serializers import (
    ContactMessageSerializer,
    EducationSerializer,
    ProfileSerializer,
    ProjectSerializer,
    ServiceSerializer,
    SkillSerializer,
)


class ProfileAPIView(generics.RetrieveAPIView):

    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.first()


class SkillListAPIView(generics.ListAPIView):

    queryset = Skill.objects.all()

    serializer_class = SkillSerializer


class ServiceListAPIView(generics.ListAPIView):

    queryset = Service.objects.filter(
        active=True
    )

    serializer_class = ServiceSerializer


class ProjectListAPIView(generics.ListAPIView):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer


class ProjectDetailAPIView(generics.RetrieveAPIView):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer

    lookup_field = "slug"


class EducationListAPIView(generics.ListAPIView):

    queryset = Education.objects.all()

    serializer_class = EducationSerializer


class ContactCreateAPIView(generics.CreateAPIView):

    queryset = ContactMessage.objects.all()

    serializer_class = ContactMessageSerializer