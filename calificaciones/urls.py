from django.urls import path
from .views import (
    CalificacionListCreateView,
    CalificacionRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("", CalificacionListCreateView.as_view(), name="calificaciones-list"),
    path("<int:id>/", CalificacionRetrieveUpdateDeleteView.as_view(), name="calificaciones-detail"),
]
