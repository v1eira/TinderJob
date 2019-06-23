from django.db import models


class Filial(models.Model):
    cnpj: str = models.CharField(max_length=100)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    def __str__(self):
        return self.empresa.razaoSocial + ' | CNPJ: ' + self.cnpj
    class Meta:
        app_label = 'jobTinder'
