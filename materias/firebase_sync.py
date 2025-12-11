import firebase_admin
from firebase_admin import credentials, db
from django.conf import settings

def get_firebase_ref():
    """
    Obtiene la referencia raíz de Firebase Realtime Database.
    """
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred, {
            "databaseURL": settings.FIREBASE_DB_URL
        })

    return db.reference("/materias")


def sync_materia_to_firebase(instance):
    """
    Envía la materia a Firebase con su estructura.
    """
    ref = get_firebase_ref()
    materia_ref = ref.child(instance.id_materia)

    # Aquí estamos obteniendo el nombre de la institución directamente desde la relación ForeignKey
    institucion_name = instance.institucion.nombre if instance.institucion else "Unknown"

    data = {
        "nombre": instance.nombre,
        "profesor": instance.profesor,
        "institucion": institucion_name,  # Asegúrate de pasar solo el nombre de la institución
        "tareas": instance.tareas or {},  # Si no hay tareas, guarda un dict vacío
        "calificaciones": instance.calificaciones or {}  # Lo mismo para calificaciones
    }

    materia_ref.set(data)


def delete_materia_from_firebase(instance):
    """
    Elimina la materia del nodo de Firebase.
    """
    ref = get_firebase_ref()
    ref.child(instance.id_materia).delete()
