import django.db


class VagaEmprego(django.db.models.Model):
    nome = django.db.models.CharField(max_length=100)
    descricao = django.db.models.TextField()  #
    regimeTrabalho = django.db.models.CharField(max_length=100)
    dataPublicacao = django.db.models.DateField()
    requisitos = django.db.models.CharField(max_length=100)
    qtdVaga = django.db.models.IntegerField()
    disponibilidade = django.db.models.BooleanField()

    empresa = django.db.models.ForeignKey("Empresa")

