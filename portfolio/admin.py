from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    ContactMessage,
    Education,
    Profile,
    Project,
    Service,
    Skill,
    SiteVisit,
)


# ============================================================
# SITE VISITS
# ============================================================

@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):

    list_display = (
        "ip_address",
        "path",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "ip_address",
        "path",
        "user_agent",
    )

    readonly_fields = (
        "ip_address",
        "path",
        "user_agent",
        "created_at",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# PROFILE
# ============================================================

@admin.register(Profile)
class ProfileAdmin(TranslationAdmin):

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
        "short_bio",
        "about",
        "email",
        "phone",
        "location",
    )

    readonly_fields = (
        "updated_at",
    )


# ============================================================
# SKILL
# ============================================================

@admin.register(Skill)
class SkillAdmin(TranslationAdmin):

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


# ============================================================
# SERVICE
# ============================================================

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):

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


# ============================================================
# PROJECT
# ============================================================

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):

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


# ============================================================
# EDUCATION
# ============================================================

@admin.register(Education)
class EducationAdmin(TranslationAdmin):

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


# ============================================================
# CONTACT MESSAGES
# ============================================================

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