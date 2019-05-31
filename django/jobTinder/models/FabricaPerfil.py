from .Candidato import Candidato
from .Recrutador import Recrutador
from .Empresa import Empresa


class FabricaPerfil:

    @staticmethod
    def create_perfil(self, nome, cpf, telefone, email, senha, data_nascimento, *args):

        if len(args) > 1:
            perfil = Candidato(nome, cpf, telefone, email, senha, data_nascimento, trabalhos_passados, local_preferencia)
        else:
            perfil = Recrutador(nome, cpf, telefone, email, senha, data_nascimento, filial)

        return perfil
