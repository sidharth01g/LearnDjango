from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        'message': 'The first app'
    }
    return render(request=request, template_name='index.html', context=context)
