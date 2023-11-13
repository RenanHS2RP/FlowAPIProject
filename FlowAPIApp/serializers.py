from rest_framework import serializers
from FlowAPIApp.models import FlowSensor

class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowSensor
        fields = '__all__'