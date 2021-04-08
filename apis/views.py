from rest_framework import viewsets

from todo_app.models import Todo
from .serializers import TodoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
