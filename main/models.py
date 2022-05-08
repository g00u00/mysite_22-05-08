from django.db import models

# Create your models here.
class Abc(models.Model):
    task = models.CharField(default="Ровна ли С сумме A и B ?", max_length=256)
    a = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    c = models.IntegerField(default=0)

# python manage.py migrate
# python manage.py makemigrations



# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)



# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']

