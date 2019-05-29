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



    #def _calcularCompatibilidade():

    class Meta:
        app_label = 'jobTinder'


import copy


class Vaga(object):

    def __init__(self, name, category='Mountain Sheep'):
        self.name = name
        self.category = category

if __name__ == '__main__':
    original_sheep = Sheep('Jolly')
    print(original_sheep.name)
    print(original_sheep.category)

    cloned_sheep = copy.deepcopy(original_sheep)
    cloned_sheep.name = 'Dolly'
    print(cloned_sheep.name)
    print(cloned_sheep.category)