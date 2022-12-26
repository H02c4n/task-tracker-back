from django.shortcuts import render, HttpResponse, get_object_or_404
# Create your views here.
from .models import Task
from.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(req):
    return HttpResponse('Hi from Task Index')



@api_view(['GET','POST'])
def tasks(req):
    if req.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = TaskSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                'message' : f"{serializer.validated_data.get('task')} is created successfully..!"
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def get_put_delete_one(req, id):
    if req.method == 'GET':
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'PUT':
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(instance=task, data=req.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                'message' : f" {serializer.validated_data.get('task')} is updated successfully..!"
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        task = get_object_or_404(Task, id=id)
        task.delete()
        message ={
            "message" : f"{task} is deleted successfully...!"
        }
        return Response(message)