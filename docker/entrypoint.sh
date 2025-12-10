#!/bin/sh

echo "🟦 Iniciando entrypoint del backend Django..."

# Aplicar migraciones
echo "🟩 Aplicando migraciones..."
python manage.py migrate --noinput

# Crear superusuario automáticamente (opcional)
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
  echo "🟨 Creando superusuario (si no existe) usando script..."
  python docker/create_superuser.py || true
fi

# Levantar servidor
echo "🟪 Levantando servidor Django en 0.0.0.0:8000..."
python manage.py runserver 0.0.0.0:8000
