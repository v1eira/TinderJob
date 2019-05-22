from django.db import models

class Cidade(models.Model):
    nome: str = models.CharField(max_length=100)

    class Meta:
        app_label = 'jobTinder'

