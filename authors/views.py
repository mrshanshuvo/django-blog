from django.shortcuts import render
from .forms import AuthorsForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author


# Create your views here.
def home(request):
    if request.method == "POST":
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/authors/thank-you")
    else:
        form = AuthorsForm()
    return render(request, "authors/home.html", {"form": form})


def thank(request):
    return HttpResponse("POST Submitted Successfully!!!")


def allData(request):
    authors_data = Author.objects.all()
    return render(request, "authors/all-data.html", {"authors_data": authors_data})


def update(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        form = AuthorsForm(request.POST)
        if form.is_valid():
            author.name = form.cleaned_data["name"]
            author.email = form.cleaned_data["email"]
            author.contact_no = form.cleaned_data["contact_no"]
            author.bio = form.cleaned_data["bio"]
            author.save()
    else:
        form = AuthorsForm(
            initial={
                "name": author.name,
                "email": author.email,
                "contact_no": author.contact_no,
                "bio": author.bio,
            }
        )
    return render(request, "authors/update.html", {"form": form})


def delete(request, id):
    if request.method == "POST":
        author = Author.objects.get(id=id)
        author.delete()
    return HttpResponseRedirect("/authors/home/")
