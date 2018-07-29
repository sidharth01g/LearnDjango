from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^user_form', view=views.user_input),
    url(regex=r'^$', view=views.index),
]
