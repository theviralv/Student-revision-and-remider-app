from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.forms import CreateUserForm
from django import forms
# Create your views here.
def home_view(request):
    context = {
        "cnt" : User.objects.count()
    }
    return render(request, "registration/home.html", context)

def signup_view(request):
    form = CreateUserForm()
    context = {}
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
        else:
            context["form"] = form
            return render(request, 'registration/signup.html', context)
    context["form"] = form
    return render(request, 'registration/signup.html', context)
