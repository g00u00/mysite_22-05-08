from django.db import models

# Create your models here.
class Abc(models.Model):
    task = models.CharField(default="Равна ли С сумме A и B?", max_length=256)
    a = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    c = models.IntegerField(default=0)

    def __str__(self):
        return self.task

# python manage.py migrate
# python manage.py makemigrations

# python manage.py shell
#
# from main.models import *
# from main.models import Abc
# Abc.objects.all()
# dir(Abc.objects)
# Abc.objects.values_list()
# Abc.objects.values_list()[3]
# Abc.objects.values_list().get(id=30)
# Abc.objects.values_list().get(c=1)
# Abc.objects.values_list().filter(c=0)
# Abc.objects.values_list().order_by('c')
# Abc.objects.values_list().filter(c = 0).order_by('-id')
# dir(Abc.objects.values_list())
# Abc.objects.values_list()._values('a')[1]
# int(Abc.objects.values_list('c')[1][0]) + 15
# raw = Abc(a = 11)
# raw.save()

# ed = Abc.objects.get(id = 31)
# ed.c = 55
# ed.save()
# Abc.objects.values_list().filter(id=31)
# Abc.objects.values_list()

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

