import firebase_admin
from firebase_admin import credentials, db
from django.conf import settings

def get_firebase_ref():
    """
    Retorna referencia al nodo /calificaciones en Firebase
    """
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred, {
            "databaseURL": settings.FIREBASE_DB_URL
        })

    return db.reference("/calificaciones")


def sync_calificacion_to_firebase(instance):
    """
    Guarda o actualiza una calificación en Firebase.
    Estructura:
    calificaciones -> est_001 -> mat_001: 95
    """
    ref = get_firebase_ref()
    
    ref.child(instance.estudiante_id).child(instance.materia_id).set(instance.calificacion)


def delete_calificacion_from_firebase(instance):
    """
    Elimina una calificación puntual del estudiante.
    """
    ref = get_firebase_ref()
    ref.child(instance.estudiante_id).child(instance.materia_id).delete()
