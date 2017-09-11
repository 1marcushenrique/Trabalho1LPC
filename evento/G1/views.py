from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def home(request):
  html = """<h1>Menu</h1>
                    <ul>
                        <li><a href='/eventos'>Eventos</a></li>
                        <li><a href='/eventoCientifico/'>Evento Cientifico</a></li>
                        <li><a href='/pessoa/'>Pessoa</a></li>
                        <li><a href='/pessoaFisica/'>Pessoa Fisica</a></li>
                        <li><a href='/pessoaJuridica/'>Pessoa Juridica</a></li>
                        <li><a href='/autor/'>Autor</a></li>
                        <li><a href='/artigoCientifico/'>Artigo Cientifico</a></li>
                        <li><a href='/inscricoes/'>INSCRICOES</a></li>

                    </ul>
                """
  return HttpResponse(html)

def eventos(request):
  html = "<h1>Eventos</h1>"
  listaEvento = Evento.objects.all()
  for ev in listaEvento:
    html += "<li>{} {} {} {} {} {} {} {} {} {} {}</li>".format(ev.nome, ev.eventoPrincipal, ev.sigla, ev.dataEHoraDeInicio,
                                                            ev.palavraChave,ev.logotipo, ev.realizador,ev.cidade,ev.uf,ev.endereco,
                                                            ev.cep)

  return HttpResponse(html)

def eventosId(request, id):
  html = "<h1>Evento por ID</h1>"
  ev = Evento.objects.get(pk=id)
  html += '<li>{} {} {} {} {} {} {} {} {} {} {}</li>'.format(ev.nome, ev.eventoPrincipal, ev.sigla, ev.dataEHoraDeInicio,
                                                            ev.palavraChave,ev.logotipo, ev.realizador,ev.cidade,ev.uf,ev.endereco,
                                                            ev.cep)

  return  HttpResponse(html)


def eventoCientifico(request):
  html = "<h1>Eventos Cientificos</h1>"
  listaEvento = EventoCientifico.objects.all()
  for ev in listaEvento:
    html += "<li>{} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {}</li>".format(ev.issn,ev.nome, ev.eventoPrincipal, ev.sigla,
                                                               ev.dataEHoraDeInicio,
                                                               ev.palavraChave, ev.logotipo, ev.realizador, ev.cidade,
                                                               ev.uf, ev.endereco,
                                                               ev.cep)

  return HttpResponse(html)


def eventoCientificoId(request, id):
  html = "<h1>Evento Cientifico por ID</h1>"
  ev = EventoCientifico.objects.get(pk=id)
  html += '<li>{} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {}</li>'.format(ev.issn,ev.nome, ev.eventoPrincipal, ev.sigla, ev.dataEHoraDeInicio,
                                                            ev.palavraChave,ev.logotipo, ev.realizador,ev.cidade,ev.uf,ev.endereco,
                                                            ev.cep)

  return  HttpResponse(html)



def pessoa(request):
  html = "<h1>Pessoas</h1>"
  listaPessoa = Pessoa.objects.all()
  for p in listaPessoa:
    html += "<li>{} | {} </li>".format(p.nome, p.email)

  return HttpResponse(html)

def pessoaId(request, id):
  html = "<h1>Pessoa por ID</h1>"
  p = Pessoa.objects.get(pk=id)
  html += '<li>{} | {} </li>'.format(p.nome, p.email)

  return  HttpResponse(html)


def pessoaFisica(request):
  html = "<h1>Pessoa Fisica</h1>"
  listaPessoa = PessoaFisica.objects.all()
  for pf in listaPessoa:
    html += "<li>{} | {} | {}</li>".format(pf.nome, pf.email, pf.cpf)

  return HttpResponse(html)

def pessoaFisicaId(request, id):
  html = "<h1>Pessoa Fisica por ID</h1>"
  pf = PessoaFisica.objects.get(pk=id)
  html += '<li>{} | {} | {} </li>'.format(pf.nome, pf.email, pf.cpf)

  return  HttpResponse(html)


def pessoaJuridica(request):
  html = "<h1>Pessoa Juridica</h1>"
  listaPessoa = PessoaJuridica.objects.all()
  for pj in listaPessoa:
    html += '<li>{} | {} | {} | {}| {}</li>'.format(pj.id,pj.nome, pj.email, pj.cnpj, pj.razaoSocial)

  return HttpResponse(html)

def pessoaJuridicaId(request, id):
  html = "<h1>Pessoa Juridica por ID</h1>"
  pj = PessoaJuridica.objects.get(pk=id)
  html += '<li>{} | {} | {} | {}| {}</li>'.format(pj.id,pj.nome, pj.email, pj.cnpj, pj.razaoSocial)

  return  HttpResponse(html)


def autor(request):
  html = "<h1>Autores </h1>"
  listaAutor = Autor.objects.all()
  for a in listaAutor:
    html += '<li>{} | {} | {} | {}|</li>'.format(a.id,a.nome, a.email, a.curriculo)

  return HttpResponse(html)

def autorId(request, id):
  html = "<h1>Autores por ID</h1>"
  a = Autor.objects.get(pk=id)
  html += '<li>{} | {} | {} | {}| </li>'.format(a.id,a.nome, a.email, a.curriculo)

  return  HttpResponse(html)



def ArtigoCientifico(request):
  html = "<h1>ArtigoCientifico </h1>"
  listaArtigo = ArtigoCientifico.objects.all()
  for a in listaArtigo:
    html += '<li>{} | {} | {}|</li>'.format(a.id,a.titulo, a.autores)

  return HttpResponse(html)

def ArtigoCientificoId(request, id):
  html = "<h1>ArtigoCientifico por ID</h1>"
  a = ArtigoCientifico.objects.get(pk=id)
  html += '<li>{} | {} | {}  </li>'.format(a.id,a.titulo, a.autores)

  return  HttpResponse(html)



def inscricoes(request):
  html = "<h1>Inscricoes </h1>"
  lista = Inscricao.objects.all()
  for a in lista:
    html += '<li>{} | {} | {} | {}|</li>'.format(a.id,a.evento, a.participante, a.tipoInscricao)

  return HttpResponse(html)
