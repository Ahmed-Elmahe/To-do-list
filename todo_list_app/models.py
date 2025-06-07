from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='todo_list_app_users',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='todo_list_app_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f"Message from {self.user.username} at {self.created_at}"
