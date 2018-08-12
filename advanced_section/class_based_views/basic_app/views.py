from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

