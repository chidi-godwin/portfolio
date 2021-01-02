from django.views.generic import TemplateView
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class SkillsView(TemplateView):
    template_name = 'skills.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


def contact_view(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            subject = "Message from portfolio"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']

            recipients = ['chidieberen1998@gmail.com']

            print([message, sender])

            send_mail(subject, message, sender, recipients,)
            return HttpResponseRedirect(reverse('contact'))
    else:
        return render(request, 'contact.html')
