from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCompletionToggleView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)


app_name = "todo_list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "tasks/create",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle/",
        TaskCompletionToggleView.as_view(),
        name="task-toggle"
    ),
]
