from django.db import models


class VagaEmprego(models.Model):
    ativa: bool = models.BooleanField()
    status: str = models.CharField(max_length=40)
    descricao: str = models.CharField(max_length=50)
    remuneracao: str = models.CharField(max_length=50)
    cargaHoraria: int = models.IntegerField()
    dataCriacao = models.DateField()
    regimeTrabalho: str = models.CharField(max_length=50)
    quantidade: int = models.IntegerField()
    # keys
    recrutador = models.ForeignKey("Recrutador", on_delete=models.CASCADE)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)


    # Prototype de fato

    def clone(self):
        return VagaEmprego(self)

    # def _calcularCompatibilidade():

    class Meta:
        app_label = 'jobTinder'
