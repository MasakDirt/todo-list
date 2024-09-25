from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("deadline", )

    @property
    def is_delay(self) -> bool:
        now = timezone.now()
        return not self.is_done and self.deadline < now

    def __str__(self) -> str:
        return f"{self.content} - {self.deadline}"
