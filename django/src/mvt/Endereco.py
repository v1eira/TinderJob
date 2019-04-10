import django.db


class Endereco(django.db.models.Model):
    CEP = django.db.models.CharField(max_length=20)
    rua = django.db.models.CharField(max_length=100)
    numero = django.db.models.IntegerField()
    complemento = django.db.models.CharField(max_length=50)
    cidade = django.db.models.CharField(max_length=30)
    estado = django.db.models.CharField(max_length=30)
    pais = django.db.models.CharField(max_length=30)

