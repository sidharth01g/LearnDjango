from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from my_app.models import AccessRecord


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    webpages_list = AccessRecord.objects.order_by('date')
    context = {'access_records': webpages_list}
    return render(request=request, template_name='my_app/index.html', context=context)
