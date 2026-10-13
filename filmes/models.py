from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField()
    ano_lancamento = models.IntegerField()
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    genero = models.ForeignKey(
        Genero,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='filmes'
    )

    def __str__(self):
        return self.titulo