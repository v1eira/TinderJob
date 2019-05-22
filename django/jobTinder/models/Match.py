from django.db import models


class Match(models.Model):
    ativa: bool = models.BooleanField()
    data = models.DateField()
    dataExpiracao = models.DateField()
    #keys
    vaga = models.ForeignKey("VagaEmprego", on_delete=models.CASCADE)
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
