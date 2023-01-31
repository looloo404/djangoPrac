from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
app_name = 'hello01'
def test1(request) :
    return HttpResponse('<h1><a href="/">Hello Test1! </a></h1>')
    