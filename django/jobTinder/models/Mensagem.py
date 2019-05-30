from django.db import models
from .Observer import *

class Mensagem(models.Model):
    data = models.DateField()
    mensagem: str = models.CharField(max_length=50)
    statusRemetente: str = models.CharField(max_length=30)
    statusDestinatario: str = models.CharField(max_length=30)
    observadores = []
    #keys
    match = models.ForeignKey("Match", on_delete=models.CASCADE)
    candidato = models.ForeignKey("Candidato", on_delete=models.CASCADE)
    recrutador = models.ForeignKey("Recrutador", on_delete=models.CASCADE)

    class Meta:
        app_label = 'jobTinder'
    #Inicializador das classes.
    def __init__(self, data,mensagem:str,statusRemetente:str,statusDestinatario:str, observadores:list):
        self.data = data
        self.mensagem:str =mensagem
        self.statusRemetente = statusRemetente
        self.statusDestinatario:str = statusDestinatario
        self.observadores:list = observadores
    #Se o observador não esta na lista de observadores, adiciona.
    def attach(self, observador):
        if observador not in self.observadores:
            self.observers.append(observador)
        else:
            print('Não foi possivel adicionar: {}'.format(observador))
    #Se o Observador esta na lista de observador, remove.
    def detach(self,observador):
        if observador in self.observadores:
            self.observadores.remove(observador)
        else:
            print("Observador não encontrado.")
    #Retorna a lista de observadores.
    def __getMonitores__(self):
        return self.observadores
    #notifica todos os observadores.
    def notify(self):
        #Alerta todos os observadores
        for observer in self._observers:
            observer.update(self)
    @property
    def status(self):
        return self.statusRemetente
    @status.setter
    #Atualiza o status e notifica.
    def status(self,statusRemetente:str):
        self.statusRemetente=statusRemetente
        self.notify()