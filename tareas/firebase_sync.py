import firebase_admin
from firebase_admin import credentials, db
from django.conf import settings

def get_firebase_ref():
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred, {
            "databaseURL": settings.FIREBASE_DB_URL
        })

    return db.reference("/tareas")


def sync_tarea_to_firebase(instance):
    ref = get_firebase_ref()
    tarea_ref = ref.child(instance.id_tarea)

    data = {
        "titulo": instance.titulo,
        "descripcion": instance.descripcion,
        "fecha_entrega": instance.fecha_entrega.strftime("%Y-%m-%d"),
        "materia_id": instance.materia.id,  # Usamos el ID de la materia
        "materia_nombre": instance.materia.nombre,  # Usamos el nombre de la materia
        "institucion_id": instance.institucion.id,  # Usamos el ID de la institución
        "institucion_nombre": instance.institucion.nombre,  # Usamos el nombre de la institución
    }

    tarea_ref.set(data)


def delete_tarea_from_firebase(instance):
    ref = get_firebase_ref()
    ref.child(instance.id_tarea).delete()
