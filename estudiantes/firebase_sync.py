from firebase_admin import db

def sync_estudiante_to_firebase(est):
    ref = db.reference(f"estudiantes/{est.firebase_key}")

    data = {
        "nombre": est.usuario.get_full_name() or est.usuario.username,
        "correo": est.usuario.email,
        "matricula": est.matricula,
        "institucion": est.institucion.firebase_key,
        "materias": {}   # se llenará cuando implementemos el módulo de materias
    }

    ref.set(data)
