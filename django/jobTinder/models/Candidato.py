from django.db import models
from .Perfil import Perfil


class Candidato(Perfil):
    localPreferencia: str = models.CharField(max_length=50)
    trabalhosPassados: str = models.TextField()
    competencias = models.ForeignKey("Competencias", on_delete=models.CASCADE)

    # def pesquisarVaga():

    def __str__(self):
        return super().__str__()

    class Meta:
        app_label = 'jobTinder'
