from .button_command import button_command
from ..models import Like

class button_like(button_command):
    # usuario e alvo viriam de template

    def executar(self):
        origem = usuario.nome  # não implementado ainda
        destino = alvo.nome  # não implementado ainda
        data = datetime.now()
        Like.__init__(origem, destino, data)
        next()