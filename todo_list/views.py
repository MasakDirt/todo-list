from django.views import generic

from todo_list.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"
