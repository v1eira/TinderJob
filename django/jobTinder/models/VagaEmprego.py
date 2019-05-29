from django.db import models


class VagaEmprego(models.Model):
    ativa:bool = models.BooleanField()
    status:str = models.CharField(max_length=40)
    descricao:str = models.CharField(max_length=50)
    remuneracao:str = models.CharField(max_length=50)
    cargaHoraria:int = models.IntegerField()
    dataCriacao = models.DateField()
    regimeTrabalho:str = models.CharField(max_length=50)
    quantidade:int = models.IntegerField()
    #keys
    recrutador = models.ForeignKey("Recrutador", on_delete=models.CASCADE)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __init__(self, ativa,status,descricao,remuneracao,cargaHoraria,dataCriacao,regimeTrabalho,quantidade,recrutador,cidade):
        self.ativa =ativa
        self.status = status
        self.descricao = descricao
        self.remuneracao = remuneracao
        self.cargaHoraria = cargaHoraria
        self.dataCriacao=dataCriacao
        self.regimeTrabalho = regimeTrabalho
        self.quantidade =  quantidade
        self.recrutador = recrutador
        self.cidade = cidade

    # Getters e Setters

    @property
    def ativa(self):
        return self.ativa

    @ativa.setter
    def ativa(self, ativa):
        self.ativa = ativa

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status

    @property
    def descricao(self):
        return self.descricao

    @descricao.setter
    def descricao(self, descricao):
        self.descricao = descricao

    @property
    def remuneracao(self):
        return self.remuneracao

    @remuneracao.setter
    def remuneracao(self, remuneracao):
        self.remuneracao = remuneracao

    @property
    def cargaHoraria(self):
        return self.cargaHoraria

    @cargaHoraria.setter
    def cargaHoraria(self, cargaHoraria):
        self.cargaHoraria = cargaHoraria

    @property
    def dataCriacao(self):
        return self.dataCriacao

    @dataCriacao.setter
    def dataCriacao(self, dataCriacao):
        self.dataCriacao = dataCriacao

    @property
    def regimeTrabalho(self):
        return self.regimeTrabalho

    @regimeTrabalho.setter
    def regimeTrabalho(self, regimeTrabalho):
        self.regimeTrabalho = regimeTrabalho

    @property
    def quantidade(self):
        return self.quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.quantidade = quantidade

    @property
    def recrutador(self):
        return self.recrutador

    @recrutador.setter
    def recrutador(self, recrutador):
        self.recrutador = recrutador

    @property
    def cidade(self):
        return self.cidade

    @cidade.setter
    def cidade(self, cidade):
        self.cidade = cidade

    def clone(self):
        return VagaEmprego(self)

    #def _calcularCompatibilidade():

    class Meta:
        app_label = 'jobTinder'