from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class ProjectsView(TemplateView):
    template_name = "projects.html"

class FindsView(TemplateView):
    template_name = "finds.html"

class ExperienceView(TemplateView):
    template_name = "experience.html"

class HobbiesView(TemplateView):
    template_name = "hobbies.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class EducationView(TemplateView):
    template_name = "education.html"
