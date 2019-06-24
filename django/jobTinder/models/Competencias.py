from django.db import models


class Competencias(models.Model):
    nome: str = models.CharField(max_length=100)
    nivel: float = models.FloatField()
    areaConhecimento: str = models.CharField(max_length=50)
    descricao: str = models.CharField(max_length=50)
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    vagaEmprego = models.ForeignKey("VagaEmprego", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
    class Meta:
        app_label = 'jobTinder'
