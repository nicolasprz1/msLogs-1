from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Log
from .serializers import LogSerializer

class LoginLogView(APIView):
    def post(self, request):
        """Registrar un log de login"""
        payload = {
            "tipo": "Login",
            "evento": request.data.get("evento", "Usuario inició sesión"),
            "usuario": request.data.get("usuario"),
            "detalle": request.data.get("detalle"),
        }
        serializer = LogSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PasswordChangeLogView(APIView):
    def post(self, request):
        """Registrar un log de cambio de contraseña"""
        payload = {
            "tipo": "Cambio de contraseña",
            "evento": request.data.get("evento", "Usuario cambió su contraseña"),
            "usuario": request.data.get("usuario"),
            "detalle": request.data.get("detalle"),
        }
        serializer = LogSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountBlockLogView(APIView):
    def post(self, request):
        """Registrar un log de bloqueo de cuenta"""
        payload = {
            "tipo": "Bloqueo de cuenta",
            "evento": request.data.get("evento", "La cuenta fue bloqueada"),
            "usuario": request.data.get("usuario"),
            "detalle": request.data.get("detalle"),
        }
        serializer = LogSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportLogView(APIView):
    def get(self, request):
        """Filtrar logs por tipo, usuario o rango de fechas"""
        tipo = request.query_params.get("tipo")  # Filtrar por tipo de log
        usuario = request.query_params.get("usuario")  # Filtrar por usuario
        fecha_inicio = request.query_params.get("fecha_inicio")  # Rango de fecha inicial
        fecha_fin = request.query_params.get("fecha_fin")  # Rango de fecha final

        logs = Log.objects.all()

        if tipo:
            logs = logs.filter(tipo=tipo)
        if usuario:
            logs = logs.filter(usuario=usuario)
        if fecha_inicio and fecha_fin:
            logs = logs.filter(timestamp__range=[fecha_inicio, fecha_fin])

        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
