from modeltranslation.translator import translator, TranslationOptions

from .models import (
    Profile,
    Skill,
    Service,
    Project,
    Education,
    ContactMessage,
)


class ProfileTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "headline",
        "short_bio",
        "about",
        "location",
    )


class SkillTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


class ServiceTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )


class ProjectTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "short_description",
        "description",
    )


class EducationTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "institution",
        "description",
    )


class ContactMessageTranslationOptions(TranslationOptions):
    fields = (
        "subject",
        "message",
    )


translator.register(
    Profile,
    ProfileTranslationOptions,
)

translator.register(
    Skill,
    SkillTranslationOptions,
)

translator.register(
    Service,
    ServiceTranslationOptions,
)

translator.register(
    Project,
    ProjectTranslationOptions,
)

translator.register(
    Education,
    EducationTranslationOptions,
)

translator.register(
    ContactMessage,
    ContactMessageTranslationOptions,
)