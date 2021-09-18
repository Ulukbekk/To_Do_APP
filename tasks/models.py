from django.db import models

from users.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='task_user')
    title = models.CharField(max_length=10)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
