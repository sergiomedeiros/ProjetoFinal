from django.db import models
from acerteresultado.jogos.models import Jogos 
# Create your models here.

class Rodadas(models.Model):
	id  = models.AutoField (primary_key = True)
	nome = models.CharField(max_length=50)
	data = models.DateField()
	jogos = models.ManyToManyField(Jogos)
	data_cadastro = models.DateField()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Rodada"
		verbose_name_plural = "Rodadas"