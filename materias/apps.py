from django.apps import AppConfig

class MateriasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "materias"

    def ready(self):
        import materias.signals
