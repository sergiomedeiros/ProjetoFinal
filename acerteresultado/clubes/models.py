from django.db import models

# Create your models here.

class Clubes(models.Model):
	id  = models.AutoField (primary_key = True)
	nome = models.CharField(max_length=50)
	data_cadastro = models.DateField()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Clube"
		verbose_name_plural = "Clubes"