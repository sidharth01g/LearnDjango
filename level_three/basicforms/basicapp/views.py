from django.shortcuts import render
from . import forms
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        'message': 'Test'
    }
    return render(request=request, template_name='basicapp/index.html', context=context)


def user_input(request: HttpRequest) -> HttpResponse:
    context = {
        'form': forms.UserForm()
    }
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            print('Form validated')
            print('Name: {}'.format(form.cleaned_data['name']))
            print('Email: {}'.format(form.cleaned_data['email']))
            print('Description: {}'.format(form.cleaned_data['description']))
    return render(request=request, template_name='basicapp/form_page.html', context=context)
