from django.urls import path
from .views import (
    TareaListCreateView,
    TareaRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("", TareaListCreateView.as_view(), name="tareas-list"),
    path("<str:id_tarea>/", TareaRetrieveUpdateDeleteView.as_view(), name="tareas-detail"),
]
