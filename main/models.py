from datetime import date
from django.db import models
from django.utils import timezone

class Abc(models.Model):
    task = models.CharField(default="Равна ли С сумме A и B?", max_length=256)
    a = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    c = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now())


#pub_date = models.DateTimeField(default=timezone.now())
#    pub_date = models.DateTimeField(default=date.today())

    def __str__(self):
        return self.task

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=5)
    # class Meta:
    #     verbose_name =  'Задание'
    #     verbose_name_plural = 'Задания'

# python manage.py makemigrations
# python manage.py migrate


# python manage.py shell
# from django.db import models
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
# Abc.objects.values_list().filter(c = 0).order_by('-id')[:2]
#Abc.objects.values_list().filter(c__lte=2).order_by('-id')
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

