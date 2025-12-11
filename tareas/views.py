from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

class TareaListCreateView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class TareaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"
