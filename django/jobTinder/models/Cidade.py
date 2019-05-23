from django.db import models

class Cidade(models.Model):
    nome: str = models.CharField(max_length=100)
    estado = models.ForeignKey("Estado", on_delete=models.CASCADE)

    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'jobTinder'

