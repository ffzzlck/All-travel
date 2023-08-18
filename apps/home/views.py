from django.shortcuts import render, redirect
from .models import Title, Reason, FAQ, ReasonTitle, ReasonImage, Question, Navbar
from ..contact.models import ContactUs
from apps.contact.forms import ContactForm
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def index(request):
    contacts = ContactUs.objects.all()
    titles = Title.objects.filter(is_published=True).order_by('-id')[:1]
    reason_titles = ReasonTitle.objects.filter(is_published=True)
    reason_images = ReasonImage.objects.filter(is_published=True)
    reasons = Reason.objects.filter(is_published=True).order_by('-id')[:3]
    faqs = FAQ.objects.filter(is_published=True)[:3]
    form = ContactForm(request.POST or None)
    questions = Question.objects.filter(is_published=True)
    navbar = Navbar.objects.all()
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'contacts': contacts,
        'titles': titles,
        'reason_titles': reason_titles,
        'reason_images': reason_images,
        'reasons': reasons,
        'faqs': faqs,
        'questions': questions,
        'navbar': navbar,
        'form': form,

    }
    return render(request, 'index.html', context)


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
