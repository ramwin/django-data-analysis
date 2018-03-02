#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-03-01 17:27:01


from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'', views.AnalysisView.as_view()),
]
