from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.decorators import login_required

from .forms import ContactForm

from .models import (
    Education,
    Profile,
    Project,
    Service,
    Skill,
    SiteVisit,
    ContactMessage,
)


# ============================================================
# PROFILE
# ============================================================

def get_profile():
    return Profile.objects.first()


# ============================================================
# HOME
# ============================================================

def home(request):

    context = {
        "profile": get_profile(),

        "skills": Skill.objects.all()[:8],

        "services": Service.objects.filter(
            active=True
        )[:6],

        "projects": Project.objects.filter(
            featured=True
        )[:6],

        "educations": Education.objects.all()[:4],
    }

    return render(
        request,
        "portfolio/home.html",
        context,
    )


# ============================================================
# ABOUT
# ============================================================

def about(request):

    context = {
        "profile": get_profile(),

        "skills": Skill.objects.all(),

        "educations": Education.objects.all(),
    }

    return render(
        request,
        "portfolio/about.html",
        context,
    )


# ============================================================
# SERVICES
# ============================================================

def services(request):

    context = {
        "profile": get_profile(),

        "services": Service.objects.filter(
            active=True
        ),
    }

    return render(
        request,
        "portfolio/services.html",
        context,
    )


# ============================================================
# PROJECTS
# ============================================================

def projects(request):

    context = {
        "profile": get_profile(),

        "projects": Project.objects.all(),
    }

    return render(
        request,
        "portfolio/projects.html",
        context,
    )


# ============================================================
# PROJECT DETAIL
# ============================================================

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
    )

    return render(
        request,
        "portfolio/project_detail.html",
        {
            "profile": get_profile(),
            "project": project,
        },
    )


# ============================================================
# CONTACT
# ============================================================

def contact(request):

    profile = get_profile()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            contact_message = form.save()

            if profile and profile.email:

                send_mail(

                    subject=(
                        f"Nouveau message portfolio : "
                        f"{contact_message.subject}"
                    ),

                    message=(
                        f"Nom : {contact_message.name}\n"
                        f"E-mail : {contact_message.email}\n\n"
                        f"{contact_message.message}"
                    ),

                    from_email=None,

                    recipient_list=[
                        profile.email
                    ],

                    fail_silently=True,
                )

            messages.success(
                request,
                "Votre message a bien été envoyé. Merci !",
            )

            return redirect(
                "portfolio:contact"
            )

    else:

        form = ContactForm()

    return render(
        request,
        "portfolio/contact.html",
        {
            "profile": profile,
            "form": form,
        },
    )


# ============================================================
# DASHBOARD
# ============================================================

@login_required
def dashboard(request):

    context = {

        "profile_count":
            Profile.objects.count(),

        "project_count":
            Project.objects.count(),

        "featured_projects":
            Project.objects.filter(
                featured=True
            ).count(),

        "service_count":
            Service.objects.filter(
                active=True
            ).count(),

        "skill_count":
            Skill.objects.count(),

        "education_count":
            Education.objects.count(),

        "message_count":
            ContactMessage.objects.count(),

        "visit_count":
            SiteVisit.objects.count(),

        "recent_projects":
            Project.objects.order_by(
                "-created_at"
            )[:5],

        "recent_messages":
            ContactMessage.objects.order_by(
                "-created_at"
            )[:5],
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )


# ============================================================
# DASHBOARD LOGIN
# ============================================================

def dashboard_login(request):

    # Si déjà connecté
    if request.user.is_authenticated:

        return redirect(
            "portfolio:dashboard"
        )


    # Formulaire envoyé
    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        # Authentification
        user = authenticate(
            request,
            username=username,
            password=password,
        )


        # Connexion réussie
        if user is not None:

            login(
                request,
                user,
            )

            # Récupérer next depuis POST
            next_url = request.POST.get(
                "next"
            )

            # Sécurité :
            # ne rediriger que vers une URL locale
            if (
                next_url
                and next_url.startswith("/")
                and not next_url.startswith("//")
            ):

                return redirect(
                    next_url
                )


            return redirect(
                "portfolio:dashboard"
            )


        # Identifiants incorrects
        return render(
            request,
            "registration/login.html",
            {
                "error":
                    "Identifiants incorrects.",

                "username":
                    username,

                "next":
                    request.POST.get(
                        "next",
                        ""
                    ),
            },
        )


    # Affichage du formulaire
    return render(
        request,
        "registration/login.html",
        {
            "next":
                request.GET.get(
                    "next",
                    ""
                ),
        },
    )


# ============================================================
# DASHBOARD LOGOUT
# ============================================================

@login_required
def dashboard_logout(request):

    logout(request)

    return redirect(
        "portfolio:login"
    )