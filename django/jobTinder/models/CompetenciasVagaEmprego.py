
from django.db import models


class CompetenciasVagaEmprego(models.Model):
    vagaEmprego = models.ForeignKey("VagaEmprego", on_delete=models.CASCADE)
    competencia = models.ForeignKey("Competencias", on_delete=models.CASCADE)

    def __str__(self):
        return self.vagaEmprego.titulo + " | " + self.competencia.nome

    class Meta:
        app_label = 'jobTinder'
