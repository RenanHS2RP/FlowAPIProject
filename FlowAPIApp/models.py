from django.db import models

class FlowSensor(models.Model):
    tempo_operacao = models.DateTimeField(auto_now_add=True)
    litros_totais = models.FloatField()
    litros_por_minuto = models.FloatField()