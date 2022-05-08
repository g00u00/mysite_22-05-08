from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("mysite")

def index(request):
     return render(request, 'mysite/index.html')

def base(request):
     return render(request, 'mysite/base.html')
