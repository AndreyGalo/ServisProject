from django.apps import AppConfig


class ServisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servis'

    def ready(self):
        from .signals import create_profile, save_profile