from django.contrib import admin
# Register your models here.
from .models import Abc #Импортируем таблицу
admin.site.register(Abc) # Регистрируем в панели администратора
