"""lpc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from G1.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^eventos/(?P<id>\d+)/$',eventosId,name='evento'),
    url(r'^eventos/', eventos, name='evento'),

    url(r'^eventoCientifico/(?P<id>\d+)/$', eventoCientificoId, name='eventoCientifico'),
    url(r'^eventoCientifico/', eventoCientifico, name='eventoCientifico'),

    url(r'^pessoa/(?P<id>\d+)/$', pessoaId, name='pessoa'),
    url(r'^pessoa/', pessoa, name='pessoa'),

    url(r'^pessoaFisica/(?P<id>\d+)/$', pessoaFisicaId, name='pessoaFisica'),
    url(r'^pessoaFisica/', pessoaFisica, name='pessoaFisica'),

    url(r'^pessoaJuridica/(?P<id>\d+)/$', pessoaJuridicaId, name='pessoaJuridica'),
    url(r'^pessoaJuridica/', pessoaJuridica, name='pessoaJuridica'),

    url(r'^autor/(?P<id>\d+)/$', autorId, name='autor'),
    url(r'^autor/', autor, name='autor'),

    url(r'^artigoCientifico/(?P<id>\d+)/$', autorId, name='artigoCientifico'),
    url(r'^artigoCientifico/', autor, name='artigoCientifico'),

    url(r'^artigoCientifico/(?P<id>\d+)/$', autorId, name='artigoCientifico'),
    url(r'^artigoCientifico/', autor, name='artigoCientifico'),

    url(r'^inscricoes/', inscricoes, name='inscricoes'),

]
