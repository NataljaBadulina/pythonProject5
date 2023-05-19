from django.apps import AppConfig


class JdappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jd_app'

    def ready(self):
        from . import signals     # выполнение модуля -> регистрация сигналов