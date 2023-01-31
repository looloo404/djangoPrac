from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    print('-'*50,request,'-'*50)
    return render(request,'tags/index.html',{'name':'Kang Jee Yoon'})
    #base_dir : project_name/templates
    