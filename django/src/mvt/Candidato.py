import django.db


class Candidato(django.db.models.Model):
    CPF = django.db.models.CharField(max_length=50)
    # experiencia = models.ListField(max_length=60)
    # trabalhosPassados = models.ListField(max_length=60)
    dataNascimento = django.db.models.DateTimeField()
    localPreferencia = django.db.models.CharField(max_length=50)
    usuario = django.db.models.ForeignKey("Usuario", on_delete=django.db.models.CASCADE)

    #def criaVaga():
    #def deletaVaga():
    #def atualizaVaga():