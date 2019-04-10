from django.db import models

class PreMatch(models.Model):
    status = models.CharField(max_length=100)
    calcCompatibilidade = models.IntegerField()
    vaga = models.ForeignKey("VagadeEmprego", on_delete=models.CASCADE)
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
