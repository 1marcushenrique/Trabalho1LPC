# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome do Evento')),
                ('eventoPrincipal', models.CharField(max_length=100, verbose_name='evento Principal')),
                ('sigla', models.CharField(max_length=10, verbose_name='sigla')),
                ('dataEHoraDeInicio', models.DateTimeField(default=django.utils.timezone.now, verbose_name='hora e data Incio')),
                ('palavraChave', models.CharField(max_length=20, verbose_name='palavra chave')),
                ('logotipo', models.CharField(max_length=20, verbose_name='logotipo')),
                ('cidade', models.CharField(max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(max_length=50, verbose_name='uf')),
                ('endereco', models.CharField(max_length=200, verbose_name='endereco')),
                ('cep', models.CharField(max_length=30, verbose_name='cep')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='G1.Pessoa')),
                ('curriculo', models.CharField(max_length=200, verbose_name='curriculo')),
                ('artigos', models.ManyToManyField(to='G1.ArtigoCientifico')),
            ],
            bases=('G1.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='G1.Evento')),
                ('issn', models.CharField(max_length=100, verbose_name='issn')),
            ],
            bases=('G1.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='G1.Pessoa')),
                ('cpf', models.CharField(max_length=20, verbose_name='cpf')),
            ],
            bases=('G1.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='G1.Pessoa')),
                ('cnpj', models.CharField(max_length=20, verbose_name='cnpj')),
                ('razaoSocial', models.CharField(max_length=50, verbose_name='razao social')),
            ],
            bases=('G1.pessoa',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G1.Pessoa'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='autores',
            field=models.ManyToManyField(to='G1.Autor'),
        ),
    ]