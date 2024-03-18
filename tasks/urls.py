from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskView,
    TaskDeleteView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskView.as_view(), name="task_main"),
    path("list", TaskListView.as_view(), name="task_list"),
    path("create", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
]
