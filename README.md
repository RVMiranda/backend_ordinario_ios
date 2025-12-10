**Proyecto: Backend-app-escuela — Desarrollo (Docker)**

- **Descripción:** Proyecto Django preparado para desarrollo dentro de Docker. Este README recoge los comandos más comunes para administrar el proyecto desde tu máquina usando los contenedores.

**Run (desarrollo)**

- **Construir la imagen y levantar (logs en foreground):**

  ```bash
  docker compose build
  docker compose up
  ```

- **Levantar en segundo plano:**

  ```bash
  docker compose up -d --build
  ```

- **Parar y eliminar contenedores/redes:**
  ```bash
  docker compose down
  ```

**Comandos `manage.py` (ejecutados dentro del contenedor `django`)**

- **Crear apps (ejemplos que tienes):**

  ```bash
  docker compose exec django python manage.py startapp auth_app
  docker compose exec django python manage.py startapp estudiantes
  docker compose exec django python manage.py startapp materias
  docker compose exec django python manage.py startapp calificaciones
  docker compose exec django python manage.py startapp tareas
  docker compose exec django python manage.py startapp anuncios
  docker compose exec django python manage.py startapp whitelabel
  ```

  - Después de crear cada app: añade el nombre de la app en `INSTALLED_APPS` (en `config/settings.py`) y luego ejecuta `makemigrations`.

- **Crear migraciones y aplicar:**

  ```bash
  docker compose exec django python manage.py makemigrations
  docker compose exec django python manage.py migrate
  ```

- **Crear superusuario (interactivo):**

  docker exec django_backend python docker/create_superuser.py
- **Entrar al shell de Django (interactivo):**

  ```bash
  docker compose exec -it django python manage.py shell
  ```

- **Listar superusers desde un one-liner (no interactivo):**

  ```bash
  docker compose exec django python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); import django; django.setup(); from django.contrib.auth import get_user_model; print(list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True)))"
  ```

- **Recolectar archivos estáticos (si se usan):**
  ```bash
  docker compose exec django python manage.py collectstatic --noinput
  ```

**Instalar dependencias nuevas**

- Edita `requirements.txt` añadiendo la dependencia y luego reconstruye la imagen:
  ```bash
  # actualizar requirements.txt
  docker compose build --no-cache
  docker compose up -d
  ```

**Logs y acceso al contenedor**

- **Ver logs (seguimiento):**

  ```bash
  docker compose logs -f django
  ```

- **Abrir un shell dentro del contenedor:**
  ```bash
  docker compose exec -it django bash
  ```

**Firebase / Credenciales**

- El contenedor está configurado para usar la clave privada montada en `/run/secrets/firebase_key.json` y la variable `FIREBASE_CREDENTIALS_PATH`.
- Variables importantes en `.env`:
  - `FIREBASE_DB_URL` — URL Realtime DB (ej.: `https://...firebaseio.com`)
  - `FIREBASE_CREDENTIALS_PATH` — si no montas la ruta como en `docker-compose.yml`, puedes poner aquí la ruta dentro del contenedor.
- Comprueba la inicialización de `firebase-admin`:
  ```bash
  docker compose exec django python -c "from config.firebase import get_firebase_app; print('Firebase app:', bool(get_firebase_app()))"
  ```

**Buenas prácticas y notas**

- No subas la clave privada (`backend-app-escuela-firebase-adminsdk-*.json`) ni tu `.env` a repositorios públicos. Ya están incluidos en `.gitignore`.
- Esta configuración es para **desarrollo**. Para producción debes usar ajustes de seguridad, un servidor WSGI (Gunicorn/uWSGI), almacenamiento de secretos seguro y una base de datos gestionada.

**Comandos útiles rápidos**

- Reiniciar solo el servicio Django:
  ```bash
  docker compose restart django
  ```
- Volver a levantar forzando rebuild (cuando cambias Dockerfile o requirements):
  ```bash
  docker compose up --build -d
  ```

Si quieres, puedo añadir una pequeña vista de ejemplo que lea/escriba en Realtime DB o crear un archivo `.env.example` con las variables mínimas.

End of README
