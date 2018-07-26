from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        'message': 'Test message'
    }
    return render(request=request, template_name='my_app/index.html', context=context)