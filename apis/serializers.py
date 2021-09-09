from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"

class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_area
        fields = "__all__"