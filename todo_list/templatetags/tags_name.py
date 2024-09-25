from django import template
from django.db.models import QuerySet

from todo_list.models import Tag


register = template.Library()


@register.filter
def tags_name(tags: QuerySet[Tag]) -> str:
    return ", ".join([tag.name for tag in tags])
