from django.db import models


class Mensagem(models.Model):
    status = models.TextField()
    dataHora = models.DateTimeField()
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'