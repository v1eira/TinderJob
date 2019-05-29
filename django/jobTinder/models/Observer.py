from django.db import models
from .Perfil import Perfil

class observavel(models.Models):
    def __init__(self):
        self.observadores = []

    def __addMonitor__(self, observador):
        if observador not in self.observadores:
            self.observers.append(observador)
        else:
            print('Não foi possivel adicionar: {}'.format(observador))

    def __removeMonitor__(self,observador):
        if observador in self.observadores:
            self.observadores.remove(observador)
        else:
            print("Observador não encontrado.")

    def __getMonitores__(self):
        return self.observadores

    def update(self, message):
        print('{} got message "{}"'.format(self.observadores, message))

    class Meta:
        app_label = 'jobTinder'


class Observador(models.Models):
    def update(self,obs):
        return


class Notificacao(Observador):
    def _update(self, Observador : Observador):
        return


