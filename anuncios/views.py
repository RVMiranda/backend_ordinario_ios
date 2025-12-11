from rest_framework import generics
from .models import Anuncio
from .serializers import AnuncioSerializer

class AnuncioListCreateView(generics.ListCreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


class AnuncioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    lookup_field = "id_anuncio"
