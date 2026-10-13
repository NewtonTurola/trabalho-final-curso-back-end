from rest_framework import serializers
from .models import Genero, Filme


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome', 'descricao']


class FilmeSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer(read_only=True)

    genero_id = serializers.PrimaryKeyRelatedField(
        source='genero',
        queryset=Genero.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Filme
        fields = [
            'id',
            'titulo',
            'sinopse',
            'ano_lancamento',
            'nota',
            'disponivel',
            'criado_em',
            'genero',
            'genero_id',
        ]
        read_only_fields = ['id', 'criado_em']