
from django.db import models


class CompetenciasCandidato(models.Model):
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    competencia = models.ForeignKey("Competencias", on_delete=models.CASCADE)

    def __str__(self):
        return self.candidato.nome + " | " + self.competencia.nome

    class Meta:
        app_label = 'jobTinder'
