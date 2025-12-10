"""Proyecto placeholder main.

Este archivo no es estrictamente necesario para Django, pero lo incluyo
como punto de entrada alternativo si lo quieres ejecutar en local.
"""
from dotenv import load_dotenv
import os


def status():
    load_dotenv()
    print('DJANGO_DEBUG=', os.environ.get('DJANGO_DEBUG'))
    print('FIREBASE_DB_URL=', os.environ.get('FIREBASE_DB_URL'))


if __name__ == '__main__':
    status()
