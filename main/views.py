import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Abc
from .forms import CreateAbcForm

def index(request):
    return render(request, 'main/index.html')


# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)

def list_main(request):
    list_main = (1, 2, 3, 4, 5)
    print("\nlist_main\n", list_main)
    dict_main = {'x': 1, 'y': 2}
    print("\ndict_main\n", dict_main)
    context = {'list_main': list_main, 'dict_main': dict_main}  # будем передавать в шаблон как один общий объект
    return render(request, 'main/list_main.html', context)


def form_create(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            form.save()
            print("\nform_post:\n", form)
            return redirect('main:result')
    else:
        print("else:\n")
        form = CreateAbcForm()
        print('\nform:\n', form)
    context = {
        'form': form
    }
    print("\ncontext:\n", context)
    return render(request, 'main/form_create.html', context)


def result(request):
    row = Abc.objects.values_list().last()
    list_data = [row[2], row[3], row[4]]
    if list_data[0] + list_data[1] == list_data[2]:
        result = "равна"
    else:
        result = "не равна"
    list_data.append(result)
    list_tasks = list()
    list_tasks.append(row[1])
    print(row[1])
    print('list_tasks:', list_tasks,end=' ')
    print('list_main_result: ', list_data)

    context = {'list_tasks': list_tasks, 'list_data': list_data}
    return render(request, 'main/result.html', context)

def table(request):
    rows = Abc.objects.values_list()
    #rows = Abc.objects.values_list().filter(c=0).order_by('-id')
    print('\nrows:\n', rows)
    context = {'rows': rows}
    return render(request, 'main/table.html', context)

def table_filter(request):
    fields = Abc.objects.values()[0].keys()
    values = Abc.objects.values_list().filter(c=3, a=1).order_by('-id')
    print('\nfields:\n', fields)
    print('\nvalues:\n', values)
    context = {'fields': fields, 'values': values}
    return render(request, 'main/table_filter.html', context)


def datetime_nov(request):
    now = list()
    now.append(datetime.datetime.now())
    print('datetime.datetime.now(): ', now)
    list_main = now
    print(list_main)
    context = {'list_main': list_main}
    return render(request, 'main/datetime_now.html', context)
