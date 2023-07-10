from django.urls import path
from .views import TaskListView,  TaskupdateView, TaskDeleteView, TaskCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/', TaskCreateView.as_view(), name='task-create')
    path('tasks/<int:pk>/', TaskupdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete')
]