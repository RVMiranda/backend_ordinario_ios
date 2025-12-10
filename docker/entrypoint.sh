#!/bin/sh

echo "🟦 Iniciando entrypoint del backend Django..."

# Aplicar migraciones
echo "🟩 Aplicando migraciones..."
if python manage.py migrate --no-input; then
  echo "🟩 Migraciones aplicadas correctamente"
else
  echo "⚠️ Error aplicando migraciones — continuaré pero puede que falten tablas"
fi

# Crear superusuario automáticamente (opcional)
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  echo "🟨 Creando superusuario (si no existe) usando script..."
  # Ejecutar el script de creación de superusuario pero no detener el container si falla
  python docker/create_superuser.py || echo "⚠️ No se pudo crear superusuario (posible BD no lista)."
fi

# Levantar servidor
echo "🟪 Levantando servidor Django en 0.0.0.0:8000..."
python manage.py runserver 0.0.0.0:8000