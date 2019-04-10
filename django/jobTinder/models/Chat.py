from django.db import models


class Chat(models.Model):
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    match = models.ForeignKey("Match", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
