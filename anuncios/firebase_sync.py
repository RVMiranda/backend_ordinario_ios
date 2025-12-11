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
    ref = get_firebase_ref()

    anuncio_ref = ref.child(instance.institucion).child(instance.id_anuncio)

    data = {
        "titulo": instance.titulo,
        "descripcion": instance.descripcion,
        "fecha": instance.fecha.strftime("%Y-%m-%d")
    }

    anuncio_ref.set(data)


def delete_anuncio_from_firebase(instance):
    ref = get_firebase_ref()
    ref.child(instance.institucion).child(instance.id_anuncio).delete()
