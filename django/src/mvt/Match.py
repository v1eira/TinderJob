import django.db


class Match(django.db.models.Model):
    status = django.db.models.CharField(max_length=100)
    data = django.db.models.DateField()
    vaga = django.db.models.ForeignKey("VagadeEmprego")
    candidato = django.db.models.ForeignKey("Candidato")

