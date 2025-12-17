from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set(request):
    request.session["name"] = "shuvo"
    request.session.set_expiry(5)
    return HttpResponse("set views is called")


def get(request):
    data = request.session["name"]
    return HttpResponse(f"Session Data: {data}")


def delete(request):
    del request.session["name"]
    # request.session.flush()  # to remove all the sessions
    return HttpResponse("delete view is called")
