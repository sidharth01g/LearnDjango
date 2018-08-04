from django.conf.urls import url
from . import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    url(regex=r'^other/$', view=views.other, name='other'),
    url(regex=r'^relative/$', view=views.relative, name='relative'),
    url(regex=r'^$', view=views.index, name='index'),
]
