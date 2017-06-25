from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'bus/index.html')

def input(request, testnumber1, num2):
    return HttpResponse('<h1>' + str(testnumber1) + '</h1>' + '<h1>' + str(num2) + '</h1>')