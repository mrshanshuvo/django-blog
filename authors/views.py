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
        form = AuthorsForm(request.POST, instance=author)
        if form.is_valid():
            author.save()
            return HttpResponseRedirect("/authors/all-data/")
    else:
        form = AuthorsForm(instance=author)
    return render(request, "authors/update.html", {"form": form})


def delete(request, id):
    if request.method == "POST":
        author = Author.objects.get(id=id)
        author.delete()
    return HttpResponseRedirect("/authors/home/")
