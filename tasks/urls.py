from django.urls import path
from tasks.views import task_create_view, TaskRetrieveUpdateDeleteAPIView, tasks_list_api_view, tasks_completed_list_api_view

urlpatterns = [
    path('completed/', tasks_completed_list_api_view),
    path('<int:pk>/', TaskRetrieveUpdateDeleteAPIView.as_view()),
    path('complete/<int:pk>/', tasks_completed_list_api_view),
    path('list/', tasks_list_api_view),
    path('', task_create_view),
]

