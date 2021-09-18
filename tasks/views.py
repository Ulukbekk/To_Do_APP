from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes

from tasks.models import Task
from tasks.permissions import IsOwner
from tasks.serializers import TaskSerializer, TaskDetailSerializer
from tasks.services import TaskCreateService, TaskCompleteService
from users.models import Account


# class TaskCreateAPIView(generics.GenericAPIView):
#     service_class = TaskCreateService
#
#     def post(self, request):
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         print(request.user, title, description)
#         self.service_class.task_create(request.user, title, description)
#
#         return Response('Ok', status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def task_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        task = Task.objects.create(
            user=user,
            title=title,
            description=description,
        )

    return HttpResponse(task, status=status.HTTP_200_OK)


class TaskRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


# class TaskListAPIView(generics.ListAPIView):
#     queryset = Task.objects.get(done=0)
#     serializer_class = TaskDetailSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#
#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def tasks_list_api_view(request):
    user = request.user
    task = Task.objects.filter(user=user, done=False)
    print(task)
    serializer = TaskDetailSerializer(task, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class TaskCompleteAPIView(generics.GenericAPIView):
    service_class = TaskCompleteService

    def post(self, request, pk):
        done = request.POST.get('done')
        task = Task.objects.filter(id=pk).first()
        print(request.user, task.user)
        if request.user != task.user:
            return HttpResponse('Error', status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.service_class.task_complete(request.user, task.title, done)

        return HttpResponse('Ok', status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tasks_completed_list_api_view(request):

    user = request.user
    completed_task = Task.objects.filter(user=user, done=True)
    print(user)

    serializer = TaskDetailSerializer(completed_task, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



