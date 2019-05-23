from django.db import models

class Estado(models.Model):
    nome: str = models.CharField(max_length=100)
    sigla: str = models.CharField(max_length = 5)
    pais = models.ForeignKey("Estado", on_delete=models.CASCADE)
    
    
    def __init__(self, nome, sigla, pais):
        self.nome = nome
        self.sigla = sigla
        self.pais = pais
    
    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'jobTinder'

