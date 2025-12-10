import os
import sys


def main():
    # Asegurar que la raíz del proyecto está en sys.path para que 'config' sea importable.
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        import django
        django.setup()
    except Exception as e:
        print('Error initializing Django:', e)
        return

    from django.contrib.auth import get_user_model
    from django.db.utils import OperationalError
    User = get_user_model()

    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if not username or not password:
        print('DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set; skipping superuser creation')
        return

    try:
        if User.objects.filter(username=username).exists():
            print('Superuser already exists; skipping')
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superuser created:', username)
    except OperationalError as e:
        print('Database not ready or missing tables, skipping superuser creation:', e)
        return

if __name__ == '__main__':
    main()
