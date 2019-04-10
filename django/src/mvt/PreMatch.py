import django.db


class PreMatch(django.db.models.Model):
    status = django.db.models.CharField(max_length=100)
    calcCompatibilidade = django.db.models.IntegerField()
    vaga = django.db.models.ForeignKey("VagadeEmprego")
    candidato = django.db.models.ForeignKey("Candidato")