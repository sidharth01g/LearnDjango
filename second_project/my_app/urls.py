from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^access_records/$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
]