from django.urls import path
from .import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('list_main/', views.list_main, name='list_main'),
    path('form_create/', views.form_create, name='form_create'),
    path('result/', views.result, name='result'),
    path('table/', views.table, name='table'),
    path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
]
