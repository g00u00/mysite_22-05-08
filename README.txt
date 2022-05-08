python manage.py shell
from main.models import Abc
Abc.objects.values_list()
Abc.objects.values_list()[0][1]
row = Abc(task="t", a = 1, b = 2, c = 3)
row.save()
row.a
Abc.objects.filter(id=4).values_list()
Abc.objects.get(pk=13).task
row = Abc(task="t_onli")
row.save()
https://www.youtube.com/watch?v=e1IyzVyrLSU&list=PLLVz8aOLIOTAZAQVWjsrAZZvKydRwjTed&index=7&t=2395s
25:39