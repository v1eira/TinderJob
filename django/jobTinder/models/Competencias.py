from django.db import models

class Competencias(models.Model):
    nome:str = models.CharField(max_length=100)
    nivel:int = models.IntegerField()
    AreaConhecimento:str = models.CharField(max_length=50)
    descricao:str = models.CharField(max_length=50)

    def __init__(self, nome, nivel, area_conhecimento, descricao):
        self.nome=nome
        self.nivel= nivel
        self.AreaConhecimento= AreaConhecimento
        self.descricao=descricao

    def __str__(self):
        return self.nome
        
    class Meta:
        app_label = 'jobTinder'
