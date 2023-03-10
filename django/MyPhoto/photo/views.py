
# from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
# from .models import Photo
# from .form import PhotoForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile

# # Create your views here.
# def photo_list(request):
#     photo = Photo.objects.all()
#     return render(request, 'photo/photo_list.html', {'photos':photo})

# def photo_detail(request,pk):
#     photo = get_object_or_404(Photo,pk=pk)
#     return render(request,'photo/photo_detail.html',{'photo':photo})

# def photo_post(request):
#     if request.method == "post":
#         form = PhotoForm(request.POST)
#         if form.is_valid():
#             photo = form.save(commit = False)
#             photo.save()
           
            
            
#             return redirect('photo_detail',pk = photo.pk)
#     else:
#         form = PhotoForm()
#     return render(request, 'photo/photo_post.html',{'form':form})
            
# def photo_edit(request,pk):
#     photo = get_object_or_404(Photo,pk=pk)
#     if request.method == 'GET':
#         form = PhotoForm(instance = photo)
#     elif request.method == 'POST':
#         form = PhotoForm(request.POST, instance = photo)
#         if form.is_valid():
#             photo = form.save(commit= False)
#             #틀로써 저장
#             photo.save()
#             upload_file = request.Files['imagefile']
#             default_storage.save(upload_file.name, ContentFile(upload_file.read()))
#             Photo.objects.filter(id = pk ).update(imagefile = upload_file)
            
#             return redirect('photo_detail',pk=photo.pk)
             
#             return redirect('photo_detail',pk = photo.id)
#     # return render(request,'photo/photo_post.html',{'form':form})
#     return render(request, 'photo/photo_post.html')

# def delete_proc(request, id):
#     Photo.objects.get(id=id).delete()
#     Photo_all = Photo.objects.all()
#     # return redirect('photo_list',{'photos':Photo_all })
#     return redirect('photo_list')

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Photo
from .form import PhotoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def photo_list(request):
    photos = Photo.objects.all().order_by('-id')
    return render(request, 'photo/photo_list.html', {'photos': photos})


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})


def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            upload_file = request.FILES['imagefile']
            default_storage.save(upload_file.name, ContentFile(upload_file.read()))
            Photo.objects.filter(id=photo.id).update(imagefile=upload_file)
            return redirect('photo_detail', pk=photo.id)

    else:
        form = PhotoForm()
        
    return render(request, 'photo/photo_post.html', {'form': form})


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST,instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            upload_file = request.FILES['imagefile']
            default_storage.save(upload_file.name, ContentFile(upload_file.read()))
            Photo.objects.filter(id=pk).update(imagefile=upload_file)

            return redirect('photo_detail', pk=photo.pk)
            
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form': form})

# def upload_proc(request):
#     upload_file = request.FILES['imagefile']
#     uploaded = default_storage.save(upload_file.name, ContentFile(upload_file.read()))

#     return render(request,'download.html',{'filename':uploaded})

def photo_delete(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    
    return redirect('photo:photo_list')


def download_proc(request,filename):
    return HttpResponse(default_storage.open(filename).read(),
        content_type='application/force-downlaod')

        #content_type='application/force-downlaod' => 다운로드 할수 있도록 하는 타입    