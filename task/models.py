from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", verbose_name=_("user"))
    title = models.CharField(max_length=200, verbose_name=_("title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    completed = models.BooleanField(default=False, verbose_name=_("completed"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
        ordering = ['-created_at']
