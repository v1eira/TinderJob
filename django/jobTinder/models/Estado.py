from django.db import models


class Estado(models.Model):
    nome: str = models.CharField(max_length=100)
    sigla: str = models.CharField(max_length=3)
    pais = models.ForeignKey("Pais", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'jobTinder'
