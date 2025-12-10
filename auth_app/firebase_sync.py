from firebase_admin import db

def sync_user_to_firebase(user):
    ref = db.reference(f"auth/{user.id}")
    data = {
        "correo": user.email,
        "rol": user.role,
        "institucion": user.institucion
    }
    ref.set(data)
