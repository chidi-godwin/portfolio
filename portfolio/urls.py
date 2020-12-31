from django.urls import path
from .views import IndexView, AboutView, SkillsView, ProjectsView, ContactView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name="about"),
    path('skills', SkillsView.as_view(), name="skills"),
    path('projects', ProjectsView.as_view(), name="projects"),
    path('contact', ContactView.as_view(), name='contact'),
]
