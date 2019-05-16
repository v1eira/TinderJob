from django.db import models


class Chat(models.Model):
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    sede = models.ForeignKey("Sede", on_delete=models.CASCADE)
    match = models.ForeignKey("Match", on_delete=models.CASCADE)

    def __init__(self, candidato, empresa, match, mensagem, data):
        self.candidato = candidato
        self.empresa = empresa
        self.match = match
        self.mensagem = mensagem
        self.data = data

    class Meta:
        app_label = 'jobTinder'
