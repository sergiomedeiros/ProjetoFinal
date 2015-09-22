from django.db import models
# Importando o padrao de usuario do django
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	time_torce = models.CharField(max_length=20)
	#foto = models.ImageField(upload_to="media/profile",blank=True) #pip install Pillow
	data_nascimento = models.DateTimeField()
	data_cadastro = models.DateTimeField(auto_now_add=True)


	def __str_(self):
		return self.user.first_name


