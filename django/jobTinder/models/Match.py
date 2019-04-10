from django.db import models


class Match(models.Model):
    status = models.CharField(max_length=100)
    data = models.DateField()
    vaga = models.ForeignKey("VagaEmprego", on_delete=models.CASCADE)
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
