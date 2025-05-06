from rest_framework import generics
from .models import Projeto
from .serializers import *

class ProjetoCreateView(generics.CreateAPIView):
    serializer_class = ProjetoSerializer


class ProjetoListView(generics.ListAPIView):
    serializer_class = ProjetoSerializer

    def get_queryset(self):
        return Projeto.objects.all()



class ProjetoTesteCreateView(generics.CreateAPIView):
    serializer_class = ProjetoTesteSerializer


class ProjetoTesteListView(generics.ListAPIView):
    serializer_class = ProjetoTesteSerializer

    def get_queryset(self):
        return Projeto.objects.all()

