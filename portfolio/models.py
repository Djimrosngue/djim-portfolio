from django.db import models
from django.urls import reverse


class Profile(models.Model):
    name = models.CharField(
        max_length=150,
        default="Djimrosngue Ngarhodjim Justin",
    )

    headline = models.CharField(
        max_length=250,
        default="IT Support | Systèmes & Réseaux | Full-Stack | IoT",
    )

    short_bio = models.TextField(
        default=(
            "Passionné par les technologies, le développement logiciel, "
            "les systèmes informatiques et l'IoT."
        )
    )

    about = models.TextField(
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
    )

    location = models.CharField(
        max_length=150,
        default="N'Djamena, Tchad",
    )

    linkedin = models.URLField(
        blank=True,
    )

    github = models.URLField(
        blank=True,
    )

    whatsapp = models.CharField(
        max_length=50,
        blank=True,
    )

    cv = models.FileField(
        upload_to="cv/",
        blank=True,
        null=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("IT", "IT Support"),
        ("NETWORK", "Réseaux"),
        ("BACKEND", "Backend"),
        ("MOBILE", "Mobile"),
        ("WEB", "Web"),
        ("IOT", "IoT"),
        ("DATA", "Data"),
        ("OTHER", "Autre"),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="OTHER",
    )

    level = models.PositiveIntegerField(
        default=70,
        help_text="Niveau de maîtrise de 0 à 100.",
    )

    description = models.TextField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)

    description = models.TextField()

    icon = models.CharField(
        max_length=50,
        default="bi-code-slash",
        help_text="Classe Bootstrap Icons.",
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
    )

    short_description = models.CharField(
        max_length=250,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Séparer les technologies par des virgules.",
    )

    github_url = models.URLField(
        blank=True,
    )

    demo_url = models.URLField(
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "portfolio:project_detail",
            kwargs={"slug": self.slug},
        )

    def technology_list(self):
        return [
            tech.strip()
            for tech in self.technologies.split(",")
            if tech.strip()
        ]


class Education(models.Model):
    title = models.CharField(
        max_length=200,
    )

    institution = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    start_year = models.PositiveIntegerField()

    end_year = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["-start_year", "order"]

    def __str__(self):
        return f"{self.title} - {self.institution}"


class ContactMessage(models.Model):
    name = models.CharField(
        max_length=150,
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_read = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class SiteVisit(models.Model):
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    path = models.CharField(
        max_length=255,
    )

    user_agent = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.ip_address} - {self.path}"