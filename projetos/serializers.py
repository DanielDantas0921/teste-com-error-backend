from rest_framework import serializers
from .models import Projeto
from .models import ProjetoTeste

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'


class ProjetoTesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetoTeste
        fields = '__all__'
