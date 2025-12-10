from django.apps import AppConfig


class WhitelabelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'whitelabel'

    def ready(self):
        import whitelabel.signals