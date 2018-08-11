from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    # url 'name' parameter is used within HTML when we user,
    # for example {% url 'basic_app:user_login' %}
    url(regex=r'^logout', view=views.user_logout, name='user_logout'),
    url(regex=r'^login/', view=views.user_login, name='user_login'),
    url(regex=r'^register/', view=views.register, name='register'),

]
