from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_Hello(request):
    x = 1
    y = 2
    c = +y
    return render(request ,'hello.html',{"name":c})

