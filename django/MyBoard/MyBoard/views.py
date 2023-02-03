from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MyBoard
from .models import MyMember
from django.utils import timezone
from django.core.paginator import Paginator


def index(request) :
    
    
    
    myBoard_all = MyBoard.objects.all().order_by('-id')
    #select * from MyBoard_MyBoard
    
    paginator = Paginator(myBoard_all,5)
    #5개씩 가져올것이다.
    page_num = request.GET.get('page','1') #default 1
    page_obj = paginator.get_page(page_num)#페이지에 맞는 모델
    
    #총개시물 수
    print('*'*30,'count','*'*30)
    print(page_obj.count)

    print('*'*30,'number 현재 페이지 번호','*'*30)
    print(page_obj.number)
    print('*'*30,'numpages 총페이지수','*'*30)
    print(page_obj.paginator.num_pages)
    
    #총페이지 range객g체
    print('----------총 페이지 range 객체----------')
    print(page_obj.paginator.page_range)
    
    print('--------------다음 페이지, 이전 페이지 ------------')
    print(page_obj.has_next)
    print(page_obj.has_previous)
    
    try:
        print('-----------다음 페이지 숫자 업으면 에러-----------')
        print(page_obj.next_page_number)
        
        print('-----------이전 페이지 숫자 없으면 에러 -------------')
        print(page_obj.previous_page_number)
        
    except:
        pass
    
    
    print('--------------start index -------------------')
    print(page_obj.start_index)
    print('---------------end index -----------------')
    print(page_obj.end_index)
    
    
    
  
    # return render(request,'index.html',{'board_all':myBoard_all})
    return render(request,'index.html',{'board_all':page_obj})

    #base_dir : project_name/templates
    #rendor 리턴값이 httpResponse 임
    
    
    
    
    
    
def insert_form(request):
    return render(request,'insert_form.html')


def insert_proc(request):
        name = request.POST['myname']
        title = request.POST['mytitle']
        content = request.POST['mycontent']
        
        result = MyBoard.objects.create(myname = name, mytitle = title, mycontent = content,mydate = timezone.now())
        # MyBoard.objects.create(myname = 'kang', mytitle = 'jw', mycontent = 'fucked me',mydate = timezone.now())
        #result 성공하면 str 실패하면 null값
        print('*'*100,result,'*'*100)
        if result :
            return redirect('index1')
            #return redirect('/')
        else:
            return redirect('forminsert')
            #return redirect('/insert_form')
            
            
def detail (request,id):
    dto = MyBoard.objects.get(id=id)
    return render(request, 'detail.html',{'dto': dto})   

def delete_proc(request,id):
    result = MyBoard.objects.get(id=id).delete()
    print(result)
    
    if result[0] :
        return redirect('index1')
    
    
def update_proc(request,id):
    post = MyBoard.objects.get(id=id)
    return render(request,'updateform.html',{'dto':post})

def updateRes(request,id):
    title = request.POST['mytitle']
    name = request.POST['myname']
    content = request.POST['mycontent']
    id = request.POST['id']
    
    post = MyBoard.objects.filter(id=id)
    result1 = post.update(mytitle = title)
    result2 = post.update(myname = name)
    result3 = post.update(mycontent = content)
    
    if result1+result2+result3 ==3  :
        return redirect('detail',id=id)
    

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        name = request.POST['myname']
        password = request.POST['mypassword'] 
        email = request.POST['myemail'] 
        
        result = MyMember.objects.create(myname = name, 
                                         mypassword=password,myemail= email )
        
        return redirect('index1')
        
    
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        
        mymember = MyMember.objects.get(myname = myname)
        
        if mypassword == mymember.mypassword :
            #본래는 암호화해서 넣는다.
            #서버에서는 암호화 해제해서 약속된 값이 있을 경우 통신연결한다.
            #성공했으니 로그인이 된 페이지
            #모든 페이지들이 세션을 통해서 로그인이 됐는지 확인한다.
            #세션은 일정시간이 되면 기록이사라진다 단 이건 개발자단에서 해결하는 것이 아니다.
            request.session['myname'] = mymember.myname
            return redirect('index1')
        else :
            #다시 로그인 페이지
            return redirect('login') 
        

def logout(request):
    del request.session['myname']
    return redirect('index1')
    

    
    
    