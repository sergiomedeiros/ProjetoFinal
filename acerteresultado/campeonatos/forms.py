from django import forms

class UserForm(forms.ModelForm):
	class Meta:
		model = Campeonatos
		fields = ('descricao','temporada')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('data_cadastro')