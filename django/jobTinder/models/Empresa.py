from django.db import models
from .Perfil import Usuario


class Empresa(models.Model):
    razaoSocial:str = models.CharField(max_length=50)
    bio:str = models.CharField(max_length=120)


    class Meta:
        app_label = 'jobTinder'
        #abstract = True

    def __init__(self, razaoSocial, bio):
        self.razaoSocial = razaoSocial
        self.bio = bio

    class Meta:
        app_label = 'jobTinder'
