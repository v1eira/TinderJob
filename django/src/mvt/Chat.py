import django.db


class Chat(django.db.models.Model):
    candidato = django.db.models.ForeignKey("Candidato")
    empresa = django.db.models.ForeignKey("Empresa")
    match = django.db.models.ForeignKey("Match")
