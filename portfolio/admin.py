from django.contrib import admin

from .models import (
    ContactMessage,
    Education,
    Profile,
    Project,
    Service,
    Skill,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "headline",
        "location",
        "updated_at",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "level",
        "order",
    )

    list_filter = (
        "category",
    )

    ordering = (
        "order",
        "name",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "active",
        "order",
    )

    list_filter = (
        "active",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "featured",
        "order",
        "created_at",
    )

    list_filter = (
        "featured",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "institution",
        "start_year",
        "end_year",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )