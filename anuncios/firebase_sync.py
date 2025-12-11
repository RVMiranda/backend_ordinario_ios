import firebase_admin
from firebase_admin import credentials, db
from django.conf import settings

def get_firebase_ref():
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred, {
            "databaseURL": settings.FIREBASE_DB_URL
        })
    
    return db.reference("/anuncios")


def sync_anuncio_to_firebase(instance):
    # Asegúrate de que 'institucion' no sea vacío o None antes de construir el path
    if instance.institucion:
        institucion_name = instance.institucion.nombre  # Asegúrate de que 'nombre' es un campo válido
        ref = db.reference('anuncios')  # Definir correctamente la referencia
        anuncio_ref = ref.child(institucion_name).child(instance.id_anuncio)
        anuncio_ref.set({
            'titulo': instance.titulo,
            'descripcion': instance.descripcion,
            'fecha': instance.fecha.isoformat(),
        })
    else:
        print("Error: La institución no está definida correctamente.")


def delete_anuncio_from_firebase(instance):
    ref = get_firebase_ref()
    ref.child(instance.institucion).child(instance.id_anuncio).delete()
