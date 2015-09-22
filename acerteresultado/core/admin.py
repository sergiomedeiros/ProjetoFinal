from django.contrib import admin

# import o usurio do pdrao do django
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile, UserProfileAdmin)

