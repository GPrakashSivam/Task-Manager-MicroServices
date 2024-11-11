from django.apps import AppConfig


class TasksServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks_service'

    def ready(self):
        import tasks_service.signals
