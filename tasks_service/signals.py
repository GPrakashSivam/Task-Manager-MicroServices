from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, timedelta
import logging
from .models import Task
from notifications_service.models import Notification

#setup a logger for notifications
logger = logging.getLogger('notifications')

@receiver(post_save, sender=Task)
def task_notification_handler(sender, instance, created, **kwargs):
    """
    Notify users when
    1. New task is assigned
    2. Task is re-assigned
    3. Task's due date is within 24 hrs
    """
    assigned_user = instance.assigned_to
    today = date.today()

    #1. Notify on new Task assignment
    if created and assigned_user:
        notify_message = f"You have been assigned a new Task: '{instance.title}'"
        Notification.objects.create(
            user=assigned_user,
            task=instance,
            message=notify_message,
            type='assigned')
        
        logger.info(f"Notification created for {assigned_user.email} - {notify_message}")
    #2. Notify on Task Re-assignment
    else:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.assigned_to != instance.assigned_to:
            if assigned_user:
                notify_message = f"You have been re-assigned with the Task: {instance.title}"
                Notification.objects.create(
                    user=assigned_user,
                    task=instance,
                    message=notify_message,
                    type='re-assigned')
                logger.info(f"Reassignment notification for {assigned_user.email}: {notify_message}")
            if old_instance.assigned:
                notify_message = f"Task '{instance.title}' has been reassigned from you."
                Notification.objects.create(
                    user=old_instance.assigned_to,
                    task=instance,
                    message=notify_message,
                    type='re-assigned')
                logger.info(f"Reassignment notification for {old_instance.assigned_to.email}: {notify_message}")
            
    # 3. Notify if due date is within the next 24 hours
    if assigned_user and instance.due_date:
        due_soon_threshold = today + timedelta(days=1)
        if today < instance.due_date <= due_soon_threshold:
            message = f"The task '{instance.title}' is due within the next 24 hours."
            Notification.objects.create(
                user=assigned_user,
                task=instance,
                message=message,
                type='task_due')
            logger.info(f"Due soon notification for {assigned_user.email}: {message}")