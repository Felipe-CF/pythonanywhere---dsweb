from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField('Nome do usuário', max_length=100)
    senha = models.CharField('Senha', max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Evento(models.Model):
    nome = models.CharField('Nome do evento', max_length=100)
    duracao = ''

class Item(models.Model):
    descricao = models.TextField('Descrição')
    foto = models.ImageField(upload_to='fotos/')
    evento = models.ManyToManyField(Evento)
