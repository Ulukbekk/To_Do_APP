from django.contrib.auth.models import User

from tasks.models import Task
from users.models import Account


class TaskCreateService:
    @classmethod
    def task_create(cls, user: User, title: str, description: str) -> None:
        task = Task.objects.filter(user=user).first()
        task.title = str(title)
        task.description = description
        task.save()


class TaskCompleteService:
    @classmethod
    def task_complete(cls, user: User, title: str, done: bool) -> None:
        task = Task.objects.filter(title=title).first()
        task.done = done
        task.save()


