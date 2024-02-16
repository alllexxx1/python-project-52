from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
