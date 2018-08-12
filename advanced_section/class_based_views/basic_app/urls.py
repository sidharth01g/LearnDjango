from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(regex=r'^$', view=views.IndexView.as_view()),
    url(regex=r'^school_list/', view=views.SchoolListView.as_view(), name='school_list'),
]
