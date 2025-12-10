"""Inicializa Firebase admin para uso en el backend.

Soporta varias formas de proveer credenciales:
- `FIREBASE_SERVICE_ACCOUNT`: JSON de service account codificado en base64.
- `FIREBASE_CREDENTIALS_PATH`: ruta al archivo JSON con la clave.
- `GOOGLE_APPLICATION_CREDENTIALS`: ruta a credenciales de ADC (opcional).

Además usa `FIREBASE_DB_URL` desde el .env para la Realtime Database.
"""
import os
import json
import base64

try:
    import firebase_admin
    from firebase_admin import credentials, db
except Exception:
    firebase_admin = None


def _load_service_account_from_base64(b64: str):
    try:
        decoded = base64.b64decode(b64).decode('utf-8')
        return json.loads(decoded)
    except Exception:
        return None


def init_firebase():
    if firebase_admin is None:
        # firebase-admin not installed
        return None

    cred = None
    # 1) FIREBASE_SERVICE_ACCOUNT (base64-encoded JSON)
    b64 = os.environ.get('FIREBASE_SERVICE_ACCOUNT')
    if b64:
        sa = _load_service_account_from_base64(b64)
        if sa:
            cred = credentials.Certificate(sa)

    # 2) FIREBASE_CREDENTIALS_PATH (path to JSON file)
    if cred is None:
        path = os.environ.get('FIREBASE_CREDENTIALS_PATH')
        if path and os.path.exists(path):
            cred = credentials.Certificate(path)

    # 3) GOOGLE_APPLICATION_CREDENTIALS or Application Default
    if cred is None:
        # try application default credentials (may work if environment provides ADC)
        try:
            cred = credentials.ApplicationDefault()
        except Exception:
            cred = None

    db_url = os.environ.get('FIREBASE_DB_URL')

    try:
        if cred is not None:
            if db_url:
                app = firebase_admin.initialize_app(cred, {'databaseURL': db_url})
            else:
                app = firebase_admin.initialize_app(cred)
            return app
        elif db_url:
            # try initialize with default credentials (may raise if none available)
            try:
                app = firebase_admin.initialize_app(options={'databaseURL': db_url})
                return app
            except Exception:
                return None
    except Exception:
        return None

    return None


# Inicialización inmediata (silenciosa) para que otros módulos puedan importar
_firebase_app = init_firebase()


def get_firebase_app():
    return _firebase_app


def get_db():
    if firebase_admin is None or _firebase_app is None:
        return None
    return db
