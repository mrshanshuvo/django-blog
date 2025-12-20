from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm, LoginFrom
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/posts/home/")
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("home"))
        else:
            form = RegisterForm()

        return render(request, "accounts/register.html", {"form": form})


# def auth_login(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect("/posts/home/")
#     else:
#         if request.method == "POST":
#             form = LoginFrom(request=request, data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data["username"]
#                 password = form.cleaned_data["password"]
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     homeURL = reverse("home")
#                     login(request, user)
#                     return HttpResponseRedirect(homeURL)
#         else:
#             form = LoginFrom()
#         return render(request, "accounts/login.html", {"form": form})


# def auth_logout(request):
#     logout(request)
#     return HttpResponseRedirect("/accounts/login/")
