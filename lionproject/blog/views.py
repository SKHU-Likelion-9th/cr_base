from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id) # 찾을 수 없다는 예외처리를 해준 것임
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)



# 여기에 edit 함수 만들어 주세요







# def update(request, id):
#     update_blog = Blog.objects.get(id = id)
#     update_blog.title = request.POST['title']
#     update_blog.writer = request.POST['writer']
#     update_blog.body = request.POST['body']
#     update_blog.pub_date = timezone.now()
#     update_blog.save()
#     return redirect('detail', update_blog.id)  






    