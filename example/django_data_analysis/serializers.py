#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-03-02 16:16:22


from rest_framework import serializers

class AnalysisSerializer(serializers.Serializer):
    starttime = serializers.DateTimeField(required=False)
    endtime = serializers.DateTimeField(required=False)
    model = serializers.CharField()

    class Meta:
        fields = ["starttime", "endtime", "model"]
