from django.urls import path
from .views import (
    MateriaListCreateView,
    MateriaRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("", MateriaListCreateView.as_view(), name="materias-list"),
    path("<str:id_materia>/", MateriaRetrieveUpdateDeleteView.as_view(), name="materias-detail"),
]
