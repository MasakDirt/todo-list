from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo_list.forms import (
    TaskCreateUpdateForm,
    SearchTaskForm,
    FilterTaskForm
)
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.prefetch_related(
        "tags"
    ).order_by("is_done", "-created_at")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(object_list=object_list, **kwargs)

        content = self.request.GET.get("content", "")
        tag = self.request.GET.get("tag", "")

        context["search"] = SearchTaskForm(initial={"content": content})
        context["filter"] = FilterTaskForm(initial={"tag": tag})
        return context

    def get_queryset(self) -> QuerySet[Task]:
        queryset = super().get_queryset()
        search = SearchTaskForm(self.request.GET)
        filter = FilterTaskForm(self.request.GET)

        if search.is_valid() and search.cleaned_data["content"]:
            queryset = queryset.filter(
                content__icontains=search.cleaned_data["content"]
            )

        if filter.is_valid() and filter.cleaned_data["tag"]:
            queryset = queryset.filter(
                tags__name__icontains=filter.cleaned_data["tag"]
            )

        return queryset


class TaskCompletionToggleView(generic.View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        is_complete = request.POST.get("is_complete")
        if is_complete == "done":
            task.is_done = True
        elif is_complete == "undo":
            task.is_done = False
        task.save()
        return redirect(reverse("todo_list:task-list"))


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateUpdateForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateUpdateForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
