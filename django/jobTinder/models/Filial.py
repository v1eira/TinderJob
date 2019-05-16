from django.db import models
from .Usuario import Usuario


class Filial(models.Model):
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
        #abstract = True

    def __init__(self, endereco, empresa):
        self.endereco = endereco
        self.empresa = empresa

    class Meta:
        app_label = 'jobTinder'
