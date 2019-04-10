from django.db import models


class Candidato(models.Model):
    CPF = models.CharField(max_length=50)
    # experiencia = models.ListField(max_length=60)
    # trabalhosPassados = models.ListField(max_length=60)
    dataNascimento = models.DateTimeField()
    localPreferencia = models.CharField(max_length=50)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    #def criaVaga():
    #def deletaVaga():
    #def atualizaVaga():

    class Meta:
        app_label = 'jobTinder'