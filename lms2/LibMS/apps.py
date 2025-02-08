from django.apps import AppConfig


class LibmsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "LibMS"
   

    def ready(self):
        from .reminder_scheduler import start_scheduler
        start_scheduler()
