from django.shortcuts import render,redirect,get_object_or_404
from .models import Board,Comment
from .forms import BoardForm,BoardDetailForm
from django.http import JsonResponse
# Create your views here.

def b_list(request):
    
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        return render(request,'bbs/list.html',{'posts':posts})
    else:
        return redirect('home')
    
    
def b_create(request):
    if request.method == 'GET' :
        board_form = BoardForm()
    else :
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()
            return redirect('bbs:b_list') 
    
        
    return render(request, 'bbs/create.html',{
        'board_form':board_form
    })
    
def b_detail(request,board_id):
    post = get_object_or_404(Board, id = board_id)
    comments = Comment.objects.all()
    board_detail_form = BoardDetailForm(instance = post)
    board_detail_form.show_board_detail()
    #입력양식이 모두 read only로 변경
    
    return render(request, 'bbs/detail.html',{'board_detail_form':board_detail_form,'comments':comments})
    
    
def b_update(request,board_id):
    post = get_object_or_404(Board, id = board_id) #post하나 가져오고
    board_detail_form = BoardDetailForm(instance = post) # 가져온 post로 값이 있는 폼 만들기
    
    board_detail_form.show_board_update() # 글 제목, 작성자, 내용만 수정처리됨
    
    return render(request, 'bbs/update.html',
                  {'board_detail_form':board_detail_form})

    
    
def b_update_process(request,board_id):
    #수정처리 되기 전의 post
    post = get_object_or_404(Board,id = board_id)
  
    if request.method == 'POST':
        # 수정된 내용을 가지고 있는 ModelForm객체를 생성한다.
        board_detail_form = BoardDetailForm(request.POST,instance=  post)
        
        if board_detail_form.is_valid():
            board_detail_form.save()
            board_detail_form.show_board_detail() # 모두 readonly변경
            return render(request, 'bbs/detail.html',{'board_detail_form':board_detail_form})
        
        return redirect('home')



def b_delete(request,board_id):
    post = get_object_or_404(Board, id = board_id)
    post.delete()
    return redirect('bbs:b_list')
    # return render(request,'bbs/list.html,)...   
    
    
            

def b_like(request,board_id):
    post = get_object_or_404(Board,id = board_id)
    post.b_like_count +=1
    post.b_author = 'seo'
    post.save()
    
    # #트랜잭션 처리를 하고 싶다면, 모델폼 객체를 사용해야함
    board_detail_form = BoardDetailForm(instance = post)
    
    new_post = board_detail_form.save(commit=False)
    print('*'*100,new_post,'*'*50)
    new_post.save()
    
    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()
    return render(request, 'bbs/detail.html',{'board_detail_form':board_detail_form})

def c_create(request):
    comment = Comment()
    comment.c_author = request.GET['user_name']
    comment.c_content = request.GET['user_content']
    comment.board_id = request.GET['board_id']
    comment.save()
    
    return JsonResponse({
            'comment_author':request.GET['user_name'],
            'comment_content': request.GET['user_content'],
            'comment_id':request.GET['board_id']
            
        },json_dumps_params={'ensure_ascii':True})
    
# def c_create(request):
    
#     # from .models import Board, Comment
#     # from django.http import JsonResponse    
#     comment = Comment()
#     comment.c_author = request.GET['user_name']
#     comment.c_content = request.GET['user_content']
#     comment.board_id = request.GET['board_id']

#     print ('---------------------------')
#     print (request.GET['board_id'])
#     print (comment.c_author)
#     print (comment.c_content)
#     print (comment.board_id)
#     print ('---------------------------')

#     comment.save()

#     return JsonResponse({
#         'comment_author': request.GET['user_name'],
#         'comment_content': request.GET['user_content'],
#         'comment_id': request.GET['board_id']
#     }, json_dumps_params= { 'ensure_ascii' : True } )
    
    
    