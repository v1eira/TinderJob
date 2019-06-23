from django.db import models
from .Mensagem import Mensagem


class Observer(models.Model):
    # Alerta o status
    @staticmethod
    def update(msg: Mensagem):

        if msg.statusRemetente == 'Não lida':
            print("Mensagem não foi lida")
            return False
        else:
            print("Mensagem não foi lida")
            return True

    class Meta:
        app_label = 'jobTinder'
