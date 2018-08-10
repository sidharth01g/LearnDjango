from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from basic_app.forms import UserForm, UserProfileInfoForm


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="basic_app/index.html")


def register(request: HttpRequest) -> HttpResponse:
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            # Hash the password using 'set_password' method
            user.set_password(user.password)

            # Save the model to DB
            user.save()

            # Save profile form without committing
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            context = {
                'error_message': 'There seems to be an error in the form you filled. Please retry'
            }
            print(user_form.errors)
            print(profile_form.errors)
            return render(request=request, template_name='basic_app/registration.html', context=context)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request=request, template_name='basic_app/registration.html', context=context)
