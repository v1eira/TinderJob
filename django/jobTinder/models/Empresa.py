from django.db import models
from .Perfil import Usuario


class Empresa(models.Model):
    razaoSocial:str = models.CharField(max_length=50)
    bio:str = models.CharField(max_length=120)

    def __init__(self, razao_social, bio):
        self.razaoSocial = razaoSocial
        self.bio = bio

    def __str__(self):
        return self.razaoSocial
    
    class Meta:
        app_label = 'jobTinder'
