from rest_framework import viewsets
from FlowAPIApp.serializers.sensoSerializer import FlowSerializer
from FlowAPIApp.models.sensorModel import FlowSensor

class FlowView(viewsets.ModelViewSet):
    queryset = FlowSensor.objects.all()
    serializer_class = FlowSerializer
