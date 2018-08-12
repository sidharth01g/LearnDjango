from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View


class AppView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name='basic_app/index.html', context={})
