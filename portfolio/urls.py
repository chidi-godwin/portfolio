from django.urls import path
from .views import IndexView, AboutView, SkillsView, ProjectsView, contact_view


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name="about"),
    path('skills', SkillsView.as_view(), name="skills"),
    path('projects', ProjectsView.as_view(), name="projects"),
    path('contact', contact_view, name='contact'),
]
