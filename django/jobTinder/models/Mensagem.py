from django.db import models


class Mensagem(models.Model):
    status = models.TextField()
    dataHora = models.DateTimeField()
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'

    def __init__(self, status, dataHora, candidato, empresa):
        self.status = status
        self.dataHora = dataHora
        self.candidato = candidato
        self.empresa = empresa