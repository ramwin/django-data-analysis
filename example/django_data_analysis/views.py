from django.shortcuts import render
from rest_framework.generics import GenericAPIView

# Create your views here.

from . import models

from django.db.models.base import ModelBase


class AnalysisModelAdmin(object):
    """"""

    def __init__(self, model_class, time_field_name):
        self.model = model_class
        self.time_field_name = time_field_name or "time"
        self.name = model_class._meta.verbose_name_plural
        self.module_name = model_class.__module__
        self.class_name = model_class.__name__


class AnalysisSite(object):
    def __init__(self):
        self.models = []
        pass

    def register(self, model, time_field_name=None):
        assert isinstance(model, ModelBase)
        analysis_model_admin = AnalysisModelAdmin(model, time_field_name=time_field_name)
        self.models.append(analysis_model_admin)


analysis_site = AnalysisSite()
analysis_site.register(models.Order, time_field_name="createtime")


class AnalysisView(GenericAPIView):

    def get_context_data(self, *args, **kwargs):
        context = {"analysis_site": analysis_site}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, "django_data_analysis/analysis.html", context)
