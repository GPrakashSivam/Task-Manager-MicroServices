from django.db import models
from users_service.models import User
from tasks_service.models import Task

class Notification(models.Model):
    NOTIFY_TYPES = [
        ('assigned','Assigned Task'),
        ('re-assigned','Re-assigned Task'),
        ('task_due','Task Due'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    task = models.ForeignKey(Task,on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    type = models.CharField(max_length=20, choices=NOTIFY_TYPES)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'

    def __str__(self):
        return f"Notification for {self.user}--{self.type} >>> {self.message}"
    