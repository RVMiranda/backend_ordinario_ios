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

    data = {
        "nombre": instance.nombre,
        "profesor": instance.profesor,
        "institucion": instance.institucion,
        "tareas": instance.tareas or {},
        "calificaciones": instance.calificaciones or {}
    }

    materia_ref.set(data)


def delete_materia_from_firebase(instance):
    """
    Elimina la materia del nodo de Firebase.
    """
    ref = get_firebase_ref()
    ref.child(instance.id_materia).delete()
