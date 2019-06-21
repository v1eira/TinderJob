from django.db import models

class Like(models.Model):
    origem: str = models.CharField(max_length=50)
    destino: str = models.CharField(max_length=50)
    data = models.DateField()

    def __init__(self, origem, destino, data):
        self.origem = origem
        self.destino = destino
        self.data = data