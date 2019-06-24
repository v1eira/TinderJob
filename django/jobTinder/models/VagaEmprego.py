from django.db import models


class VagaEmprego(models.Model):
    ativa: bool = models.BooleanField()
    titulo: str = models.CharField(max_length=50)
    descricao: str = models.CharField(max_length=1000)
    remuneracao: str = models.CharField(max_length=50)
    cargaHoraria: int = models.IntegerField()
    dataCriacao = models.DateField()
    regimeTrabalho: str = models.CharField(max_length=500)
    quantidade: int = models.IntegerField()
    # keys
    recrutador = models.ForeignKey("Recrutador", on_delete=models.CASCADE)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __str__(self):
        return "Vaga" + self.recrutador.filial

    # Prototype de fato
    def clone(self):
        return VagaEmprego(self)

    # def _calcularCompatibilidade(competencias: Competencias):

    class Meta:
        app_label = 'jobTinder'
