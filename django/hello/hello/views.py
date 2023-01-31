from django.shortcuts import render
from django.http import HttpResponse

def test(request) :
    return HttpResponse('<h1><a href = "/">Hello, Test!</a><h1>')

def index(request):
    return HttpResponse('<h1>Hello, World! </h1>')