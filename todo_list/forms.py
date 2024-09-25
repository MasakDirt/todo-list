from django import forms

from todo_list.models import Task, Tag


class TaskCreateUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")


class SearchTaskForm(forms.Form):
    content = forms.CharField(
        required=False,
        max_length=100,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by content",
                "class": "form-control"
            }
        )
    )


def tag_choices() -> list:
    return [("", "Select tag")] + [
        (tag.name, tag.name.capitalize())
        for tag in Tag.objects.all()
    ]


class FilterTaskForm(forms.Form):
    tag = forms.ChoiceField(
        choices=tag_choices(),
        required=False,
        label=""
    )
