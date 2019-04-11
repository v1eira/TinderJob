from .Candidato import Candidato
from .Empresa import Empresa


class FabricaUsuario:

    @staticmethod
    def get_usuario(self, tipo_usuario, nome, email, senha):

        if tipo_usuario.lower() == 'candidato':
            usuario = Candidato(nome, email, senha)
        elif tipo_usuario.lower() == 'empresa':
            usuario = Empresa(nome, email, senha)

        return usuario
