from rest_framework import generics
from .models import Materia
from .serializers import MateriaSerializer

class MateriaListCreateView(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class MateriaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    lookup_field = "id_materia"
