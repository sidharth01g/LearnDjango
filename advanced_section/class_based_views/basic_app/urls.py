from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(regex=r'^$', view=views.IndexView.as_view()),
    url(regex=r'^school_list/(?P<pk>[-\w]+)$', view=views.SchoolDetailView.as_view(), name='school_detail'),
    url(regex=r'^school_list/$', view=views.SchoolListView.as_view(), name='school_list'),
    url(regex=r'^school_create/$', view=views.SchoolCreateView.as_view(), name='school_create'),
    url(regex=r'^school_update/(?P<pk>[-\w]+)$', view=views.SchoolUpdateView.as_view(), name='school_update'),
]
