from firebase_admin import db

def sync_institution_to_firebase(inst):
    ref = db.reference(f"whitelabel/{inst.firebase_key}")

    data = {
        "nombre": inst.nombre,
        "logo_url": inst.logo_url,
        "colores": {
            "primario": inst.color_primario,
            "secundario": inst.color_secundario,
            "fondo": inst.color_fondo,
            "texto": inst.color_texto,
        },
        "textos": {
            "bienvenida": inst.texto_bienvenida,
            "descripcion": inst.texto_descripcion,
        },
        "config": {
            "mostrar_anuncios": inst.mostrar_anuncios,
            "mostrar_tareas": inst.mostrar_tareas,
            "mostrar_calificaciones": inst.mostrar_calificaciones,
        }
    }

    ref.set(data)
