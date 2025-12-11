from django.urls import path
from .views import (
    AnuncioListCreateView,
    AnuncioRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("", AnuncioListCreateView.as_view(), name="anuncios-list"),
    path("<str:id_anuncio>/", AnuncioRetrieveUpdateDeleteView.as_view(), name="anuncios-detail"),
]
