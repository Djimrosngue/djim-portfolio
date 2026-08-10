from django.contrib import admin

from .models import (
    ContactMessage,
    Education,
    Profile,
    Project,
    Service,
    Skill,
    SiteVisit,
)

admin.site.register(SiteVisit)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "headline",
        "email",
        "phone",
        "location",
        "updated_at",
    )

    search_fields = (
        "name",
        "headline",
        "email",
        "phone",
        "location",
    )

    readonly_fields = (
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

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "level",
        "order",
    )

    ordering = (
        "order",
        "name",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon",
        "active",
        "order",
    )

    list_filter = (
        "active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "active",
        "order",
    )

    ordering = (
        "order",
        "title",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "featured",
        "order",
        "created_at",
    )

    list_filter = (
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "technologies",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    list_editable = (
        "featured",
        "order",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "institution",
        "start_year",
        "end_year",
        "order",
    )

    search_fields = (
        "title",
        "institution",
        "description",
    )

    list_editable = (
        "start_year",
        "end_year",
        "order",
    )

    ordering = (
        "-start_year",
        "order",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )