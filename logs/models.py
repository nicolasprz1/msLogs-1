from django.db import models

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora del log
    tipo = models.CharField(max_length=50)  # Tipo de evento (Autenticación, Pago, etc.)
    evento = models.CharField(max_length=100)  # Descripción breve del evento
    usuario = models.CharField(max_length=50, null=True, blank=True)  # Usuario relacionado
    tenant = models.CharField(max_length=50, null=True, blank=True)  # Tenant relacionado (opcional)
    detalle = models.TextField(null=True, blank=True)  # Información adicional

    def __str__(self):
        return f"{self.timestamp} - {self.tipo}: {self.evento}"
