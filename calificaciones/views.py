from rest_framework import generics
from .models import Calificacion
from .serializers import CalificacionSerializer

class CalificacionListCreateView(generics.ListCreateAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer


class CalificacionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    lookup_field = "id"  # Usamos ID interno de Django
