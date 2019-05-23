from django.db import models


class Mensagem(models.Model):
    data = models.DateField()
    mensagem:str = models.CharField(max_length=50)
    #keys
    match = models.ForeignKey("Match", on_delete=models.CASCADE)
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    recrutador = models.ForeignKey("Recrutador", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'

    def __init__(self, data,mensagem):
        self.data = data
        self.mensagem=mensagem