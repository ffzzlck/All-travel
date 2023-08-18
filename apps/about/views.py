from django.shortcuts import render, redirect
from .models import About, Service
from ..home.models import Title, Question, Reason, Navbar
from ..contact.models import ContactUs
from apps.contact.forms import ContactForm


def about(request):
    contacts = ContactUs.objects.all()
    companies = About.objects.filter(is_published=True).order_by('-id')[:1]
    contracts = Service.objects.filter(is_published=True).order_by('-id')[:4]
    titles = Title.objects.filter(is_published=True)
    reasons = Reason.objects.filter(is_published=True).order_by('-id')[:3]
    questions = Question.objects.filter(is_published=True)
    navbar = Navbar.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'contacts': contacts,
        'companies': companies,
        'contracts': contracts,
        'titles': titles,
        'reasons': reasons,
        'questions': questions,
        'navbar': navbar,
        'form': form,
    }

    return render(request, 'about.html', context)
