from ..models import Like
from datetime import datetime
from .button_command import button_command


class button_like(button_command):
    # usuario e alvo viriam de template

    origem = usuario.nome # não implementado ainda
    destino = alvo.nome # não implementado ainda
    data = datetime.now()

    Like.__init__(origem, destino, data)