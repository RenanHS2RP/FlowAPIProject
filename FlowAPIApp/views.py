from rest_framework import viewsets
from FlowAPIApp.serializers import FlowSerializer
from FlowAPIApp.models import FlowSensor

class FlowView(viewsets.ModelViewSet):
    queryset = FlowSensor.objects.all()
    serializer_class = FlowSerializer
