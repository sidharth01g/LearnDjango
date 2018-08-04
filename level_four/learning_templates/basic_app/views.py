from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request=request, template_name='basic_app/index.html', context=context)


def other(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request=request, template_name='basic_app/other.html', context=context)


def relative(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request=request, template_name='basic_app/relative_url_templates.html', context=context)
