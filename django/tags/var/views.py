from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'var/index.html',{'name':'Kang Jee Yoon'})


def variable01(request):
    my_list = ['python','django','template']
    return render(request,'var/variable01.html',{'lst':my_list})

def variable02(request):
    my_dict = {'name':'Kang','class':'AI 취업'}
    return render(request,'var/variable02.html',{'dict':my_dict})

def testfor(request):
    return render(request,'var/testfor.html',{'number':range(1,11)})

def iftest(request):
    return render(request,'var/iftest.html',{'user':{'id':'gond-gd'}})

def iftest2(request):
    member = {'id':'multi','class':'ai', 'role':'manager'}
    return render(request,'var/if02.html',{'user':member})