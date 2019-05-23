from django.db import models


class VagaEmprego(models.Model):
    ativa:bool = models.BooleanField()
    status:str = models.CharField(max_length=40)
    descricao:str = models.CharField(max_length=50)
    remuneracao:str = models.CharField(max_length=50)
    cargaHoraria:int = models.IntegerField()
    dataCriacao = models.DateField()
    regimeTrabalho:str = models.CharField(max_length=50)
    quantidadeVaga:int = models.IntegerField()
    #keys
    recrutador = models.ForeignKey("Recrutador", on_delete=models.CASCADE)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __init__(self, ativa,status,descricao,remuneracao,cargaHoraria,dataCriacao,regimeTrabalho,quantidadeVaga,recrutador,cidade):
        self.ativa =ativa
        self.status = status
        self.descricao = descricao
        self.remuneracao = remuneracao
        self.cargaHoraria = cargaHoraria
        self.dataCriacao=dataCriacao
        self.regimeTrabalho = regimeTrabalho
        self.quantidadeVaga =  quantidadeVaga
        self.recrutador = recrutador
        self.cidade = cidade

    #def _calcularCompatibilidade():

    class Meta:
        app_label = 'jobTinder'