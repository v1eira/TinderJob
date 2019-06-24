from .Candidato import Candidato
from .Recrutador import Recrutador


class FabricaPerfil:

    @staticmethod
    def create_perfil(perfil: str):

        if perfil == 'cadidato':
            return Candidato()
        else:
            return Recrutador()
