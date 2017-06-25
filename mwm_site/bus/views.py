from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {"hour": "6 hours", }
    return render(request, 'bus/index.html', context)


def num_input(request, testnumber1, num2):
    return HttpResponse('<h1>' + str(testnumber1) + '</h1>' + '<h1>' + str(num2) + '</h1>')


def var_input(request, var=None):
    print(var)
    return HttpResponse(request.method + var)


def form_test(request):
    print(request.GET)
    return render(request, 'bus/index.html')