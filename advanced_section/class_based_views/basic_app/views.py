from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs) -> HttpResponse:
        context = super().get_context_data(**kwargs)
        context['message'] = 'This page uses injected context my means of TempateViews'
        return context


class SchoolListView(ListView):
    # ListView: context variable names
    # ================================
    # By default Django injects "model.School" into context via a list named "school_list" in the
    # HTML template
    # Django lowercases the variable name "School" to "school" and appends "_list" -> "school_list"
    # This variable is a list of all schools in the database
    # We can modify this default behavior by naming the list variable ourselves by using a
    # variable "context_object_name"
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    # DetailView: context varible names
    # =================================
    # Djanog lowercases "models.School" to "school"
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
