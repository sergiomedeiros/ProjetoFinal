from django.db import models

# Create your models here.
class Campeonatos(models.Model):
	id  = models.AutoField (primary_key = True)
	descricao = models.CharField(max_length=50)
	temporada = models.CharField(max_length=10)
	data_cadastro = models.DateField()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Campeonato"
		verbose_name_plural = "Campeonatos"
