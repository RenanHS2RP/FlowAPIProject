from rest_framework import viewsets
from FlowAPIApp.serializers.pumpSerializer import PumpSerializer
from FlowAPIApp.models.pumpModel import PumpFlow

class PumpView(viewsets.ModelViewSet):
    queryset = PumpFlow.objects.all()
    serializer_class = PumpSerializer
