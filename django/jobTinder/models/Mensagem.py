from django.db import models

class Mensagem(models.Model):
    status = models.TextField()
    dataHora = models.DateTimeField()
    candidato = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
