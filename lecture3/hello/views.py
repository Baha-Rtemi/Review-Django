from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    # This function takes request as argument and this argument going to 
    # represent the HTTP request that the user made in order
    # to access our web server. So if we want information about that
    # request, we can look inside of this requested object to get access
    # to some other data.
    return HttpResponse("Hello!")

def brain(request):
    return HttpResponse("Hello, Brain!")

def baha(request):
    return HttpResponse("Hello, Baha!")

# simple greet function 
# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def index(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })