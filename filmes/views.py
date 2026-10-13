from rest_framework import viewsets
from .models import Genero, Filme
from .serializers import GeneroSerializer, FilmeSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.select_related('genero').all()
    serializer_class = FilmeSerializer