from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from TodoList.TaskSerializer import TitleSerializers
from TodoList.models import Task

class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TitleSerializers(tasks, many=True)
        return Response(serializer.data)

class TaskDetailView(APIView):
    def get_in_id(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TitleSerializers(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TaskCreateView(APIView):
    def create(self, request):
        serializer = TitleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskupdateView(APIView):
    def update(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TitleSerializers(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TaskDeleteView(APIView):
    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)





