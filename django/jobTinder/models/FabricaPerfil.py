from .Candidato import Candidato
from .Empresa import Empresa


class FabricaPerfil:

    @staticmethod
    def get_perfil(self, tipo_perfil):

        if tipo_perfil.lower() == 'candidato':
            perfil = Candidato() #TODO
        elif tipo_perfil.lower() == 'recrutador':
            perfil = Recrutador() #TODO

        return perfil
