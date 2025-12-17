from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set(request):
    print("Set view is called")
    response = render(request, "cookie/home.html")
    response.set_cookie("theme", "dark")
    response.set_cookie("mr", "land")
    return response


def get(request):
    theme = request.COOKIES
    return HttpResponse(f"GET - {theme}")


def delete(request):
    response = HttpResponse("Deleted!!")
    response.delete_cookie("theme")
    return response


def update(request):
    response = HttpResponse("Updated")
    response.set_cookie("mr", "ad")
    return response
