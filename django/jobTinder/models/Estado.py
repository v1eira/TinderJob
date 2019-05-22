from django.db import models

class Estado(models.Model):
    nome: str = models.CharField(max_length=100)
    sigla: str = models.CharField(max_lenght = 5)

    class Meta:
        app_label = 'jobTinder'

