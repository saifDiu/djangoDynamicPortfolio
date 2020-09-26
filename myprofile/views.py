from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from . models import *
from .forms import ContactForm
from django.contrib import messages


def index(request):
    uservalue = myProfile.objects.all()
    countv = uservalue.count()
    works = worksarea.objects.all()
    project = projects.objects.all()
    educations = education.objects.all()
    forms = ContactForm()
    flag = 0
    if request.method == "POST":
        forms = ContactForm(request.POST)
        if forms.is_valid():
            flag += 1
            subject = forms.cleaned_data['subject']
            from_email = forms.cleaned_data['from_email']
            message = forms.cleaned_data['message']
            send_mail(
            subject + ' from : ' + from_email,
            message,
            from_email,
            ['saifislam.swe@gmail.com'],
            )
            return redirect('index')


    context = {'uservalue': uservalue, 'works':works, 'project': project,
     'educations':educations, 'forms':forms, 'flag':flag}
    return render(request, 'myprofile/index.html', context)
