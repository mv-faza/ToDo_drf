from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('tasks/', views.taskList, name="task-list"),
	path('task/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('tasks/expired/', views.TaskExpired, name='task-expired'),
    path('tasks/in_progress/', views.TaskInProgress, name='in-progress'),
    path('tasks/done/', views.TaskDone, name='done'),
]