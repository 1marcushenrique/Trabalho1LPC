# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('G1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInscricao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data da Incricao')),
                ('tipoInscricao', models.CharField(default='aluno', max_length=20, verbose_name='tipo inscricao')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G1.PessoaFisica')),
            ],
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataEHoraDeInicio',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='hora e data Inicio'),
        ),
    ]