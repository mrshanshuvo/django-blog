from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                homeURL = reverse("home")
                login(request, user)
                return HttpResponseRedirect(homeURL)
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})
