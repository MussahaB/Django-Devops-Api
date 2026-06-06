from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.db import connection
from django.db.utils import OperationalError
from django.http import JsonResponse


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def health_check(request):
    try:
        connection.cursor()

        return JsonResponse({"status": "healthy", "database": "connected"})

    except OperationalError:
        return JsonResponse(
            {"status": "unhealthy", "database": "disconnected"}, status=500
        )
