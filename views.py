from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact_page(request):
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            subject = request.POST['subject']
            message = request.POST['message']

            to_email = forms.cleaned_data.get('email')
            send_mail(subject,message, "yourmail@gmail.com", [to_email],fail_silently=False)
            messages.add_message(request, messages.INFO, 'Message sent successfully!')
            return redirect('index')
    context = {
        'forms': forms
    }
    return render(request, 'contact/contact.html', context)
