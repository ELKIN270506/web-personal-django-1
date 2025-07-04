from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "core/home.html"

class AboutView(TemplateView):
    template_name = "core/about.html"

class ProjectsView(TemplateView):
    template_name = "core/projects.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"

class SampleView(TemplateView):
    template_name = "core/sample.html"
