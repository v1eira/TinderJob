from django.db import models


class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    nomeFantasia = models.CharField(max_length=50)

    def __str__(self):
        return self.nomefantasia

    class Meta:
        app_label = 'jobTinder'
