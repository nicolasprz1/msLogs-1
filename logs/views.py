from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Log
from .serializers import LogSerializer

class LogView(APIView):
    def get(self, request):
        """Lista todos los logs almacenados."""
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea un nuevo log."""
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
