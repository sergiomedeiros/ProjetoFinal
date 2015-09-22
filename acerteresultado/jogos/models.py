from django.db import models

# Create your models here.
class Jogos(models.Model):
	id  = models.AutoField (primary_key = True)
	data = models.DateField()
	hora = models.TimeField()
	clube_casa = models.CharField(max_length=30)
	clube_visitante = models.CharField(max_length=30)
	gol_clube_casa = models.IntegerField()
	gol_clube_visitante = models.IntegerField()
	adiado = models.BooleanField()
	data_cadastro = models.DateField()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Jogo"
		verbose_name_plural = "Jogos"