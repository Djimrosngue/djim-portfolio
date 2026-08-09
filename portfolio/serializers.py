from rest_framework import serializers

from .models import (
    ContactMessage,
    Education,
    Profile,
    Project,
    Service,
    Skill,
)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    technology_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "description",
            "image",
            "technologies",
            "technology_list",
            "github_url",
            "demo_url",
            "featured",
            "order",
            "created_at",
        ]

    def get_technology_list(self, obj):
        return obj.technology_list()


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage

        fields = [
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]