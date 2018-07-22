# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    print(request)
    return HttpResponse("<h1>Welcome to the First App index page</h1>")
