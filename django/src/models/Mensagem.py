import django.db


class Mensagem(django.db.models.Model):
    status = django.db.models.TextField()
    dataHora = django.db.models.DateTimeField()
    candidato = django.db.models.ForeignKey("Usuario")
    empresa = django.db.models.ForeignKey("Usuario")