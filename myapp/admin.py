from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Registre o modelo User com o UserAdmin para personalizar a administração
admin.site.unregister(User)  # Primeiro, faça o unregister para evitar duplicidade
admin.site.register(User, UserAdmin)
