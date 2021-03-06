# Generated by Django 2.1.7 on 2019-06-24 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobTinder', '0005_auto_20190624_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenciasCandidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobTinder.Candidato')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobTinder.Competencias')),
            ],
        ),
        migrations.CreateModel(
            name='CompetenciasVagaEmprego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobTinder.Competencias')),
                ('vagaEmprego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobTinder.VagaEmprego')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('data', models.DateField()),
            ],
        ),
    ]
