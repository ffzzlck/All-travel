from django.shortcuts import render, redirect
from apps.contact.forms import ContactForm
from ..home.models import Title, Reason, Navbar
from .models import ContactUs


def contact(request):
    titles = Title.objects.filter(is_published=True)
    reasons = Reason.objects.filter(is_published=True).order_by('-id')[:3]
    contacts = ContactUs.objects.all()
    navbar = Navbar.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'titles': titles,
        'reasons': reasons,
        'contacts': contacts,
        'navbar': navbar,
        'form': form,

    }
    return render(request, 'contact.html', context)
