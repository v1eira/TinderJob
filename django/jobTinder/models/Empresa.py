from django.db import models


class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=50)
    bio = models.CharField(max_length=120)

    def __str__(self):
        return self.razaoSocial

    class Meta:
        app_label = 'jobTinder'
