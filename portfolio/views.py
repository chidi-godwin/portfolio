from django.views.generic import FormView, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class SkillsView(TemplateView):
    template_name = 'skills.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


class ContactView(FormView):
    pass
