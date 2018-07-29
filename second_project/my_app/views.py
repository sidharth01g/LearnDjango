from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from my_app.models import AccessRecord, User
from .forms import NewUserForm


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    webpages_list = AccessRecord.objects.order_by('date')
    context = {'access_records': webpages_list}
    return render(request=request, template_name='my_app/index.html', context=context)


def users(request: HttpRequest) -> HttpResponse:
    users_list = User.objects.order_by('email')
    context = {
        'users': users_list
    }
    return render(request=request, template_name='my_app/users.html', context=context)


def create_user(request: HttpRequest) -> HttpResponse:
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR: Form validation failed')

    context = {
        'user_form': form
    }

    return render(request=request, template_name='my_app/create_user.html', context=context)
