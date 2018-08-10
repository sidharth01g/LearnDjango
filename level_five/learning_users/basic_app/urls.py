from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(regex=r'^register/', view=views.register, name='register'),

]