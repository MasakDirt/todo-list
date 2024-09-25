from django.urls import path

from todo_list.views import TaskListView


app_name = "todo_list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list")
]
