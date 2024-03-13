from django.db import models

# Create your models here.

class Pergunta(models.Model):
    texto= models.CharField(max_length=200)
    data_pub = models.DateTimeField('data de publicação')

class Alternativa(models.Model):
    texto= models.CharField(max_length=250)
    quant_votos= models.IntegerField('quantidade de votos', default=0)
    pergunta_associada= models.ForeignKey(Pergunta, on_delete=models.CASCADE)