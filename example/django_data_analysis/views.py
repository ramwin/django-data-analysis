from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.

from . import models, serializers

from django.db.models.base import ModelBase
from django.db.models.functions import TruncDate
from django.db.models import Count


class AnalysisModelAdmin(object):
    """"""

    def __init__(self, model_class, time_field_name):
        self.model = model_class
        self.primary_key = 'pk'
        self.time_field_name = time_field_name or "time"
        self.name = model_class._meta.verbose_name_plural
        self.module_name = model_class.__module__
        self.class_name = model_class.__name__
        self.unique_name = "{}.{}".format(self.module_name, self.class_name)


class AnalysisSite(object):
    def __init__(self):
        self.models = []
        self.model_index = {}

    def register(self, model, time_field_name=None):
        assert isinstance(model, ModelBase)
        analysis_model_admin = AnalysisModelAdmin(model, time_field_name=time_field_name)
        self.models.append(analysis_model_admin)
        self.model_index[analysis_model_admin.unique_name] = analysis_model_admin
        assert analysis_model_admin

    def get_model_admin(self, unique_name):
        print(self.model_index)
        print(unique_name)
        return self.model_index[unique_name]


analysis_site = AnalysisSite()
analysis_site.register(models.Order, time_field_name="createtime")


class AnalysisView(GenericAPIView):

    def get_context_data(self, *args, **kwargs):
        context = {"analysis_site": analysis_site}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, "django_data_analysis/analysis.html", context)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = serializers.AnalysisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        modeladmin = analysis_site.get_model_admin(serializer.validated_data["model"])
        filter_params = {}
        if serializer["starttime"]:
            filter_params["{}__gte".format(modeladmin.time_field_name)] = serializer.validated_data["starttime"]
        if serializer["endtime"]:
            filter_params["{}__lte".format(modeladmin.time_field_name)] = serializer.validated_data["endtime"]
        queryset = modeladmin.model.objects.filter(**filter_params).distinct()
        result = queryset.annotate(
                date=TruncDate(modeladmin.time_field_name)).\
            values('date').annotate(Count(modeladmin.primary_key))
        return Response(result)
