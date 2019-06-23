
class Usuario():

    user
    senha
    perfil

    # Métodos
    def __init__(self, user, senha, perfil):
        self.user = user
        self.senha = senha
        self.perfil = perfil

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'jobTinder'
        abstract = True
