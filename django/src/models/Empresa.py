import django.db


class Empresa(django.db.models.Model):
    CNPJ = django.db.models.CharField(max_length=50)
    descricao = django.db.models.CharField(max_length=60)
    usuario = django.db.models.ForeignKey("Usuario", on_delete=django.db.models.CASCADE)

