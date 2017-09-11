from django.db import models
from django.utils import timezone

# Create your models here.

class Evento(models.Model):
  nome = models.CharField('nome do Evento', max_length=100)
  eventoPrincipal = models.CharField('evento Principal', max_length=100)
  sigla = models.CharField('sigla',max_length=10)
  dataEHoraDeInicio = models.DateTimeField('hora e data Inicio',default=timezone.now)
  palavraChave = models.CharField('palavra chave',max_length=20)
  logotipo = models.CharField('logotipo',max_length=20)
  realizador = models.ForeignKey('Pessoa')
  cidade = models.CharField('cidade',max_length=100)
  uf = models.CharField('uf',max_length=50)
  endereco = models.CharField('endereco',max_length=200)
  cep = models.CharField('cep',max_length=30)


class EventoCientifico(Evento):
  issn = models.CharField('issn',max_length=100)


class Pessoa(models.Model):
  nome = models.CharField('nome',max_length=100)
  email = models.CharField('email',max_length=50)


class PessoaFisica(Pessoa):
  cpf = models.CharField('cpf',max_length=20)


class PessoaJuridica(Pessoa):
  cnpj = models.CharField('cnpj',max_length=20)
  razaoSocial = models.CharField('razao social',max_length=50)


class Autor(Pessoa):
  curriculo = models.CharField('curriculo',max_length=200)
  artigos = models.ManyToManyField('ArtigoCientifico')


class ArtigoCientifico(models.Model):
  titulo = models.CharField('titulo',max_length=50)
  autores = models.ManyToManyField(Autor)


class TipoInscricao(models.Model):
  tipo = models.CharField("Tipo de Inscricao",max_length=20)


class Inscricao(models.Model):
  evento = models.ForeignKey(Evento)
  participante = models.ForeignKey(PessoaFisica)
  dataInscricao = models.DateTimeField("data da Incricao",default=timezone.now)
  tipoInscricao = models.ForeignKey(TipoInscricao)

