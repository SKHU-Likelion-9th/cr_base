from django.shortcuts import render, redirect, get_object_or_404 
# get_object_or_404이란 서버에 없는 페이지를 요청했을 경우 띄워주는 에러창 
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, id): # 이것도 마찬가지로 해당 글만 나와야 하므로 id를 매개변수로 받아옴
    blog = get_object_or_404(Blog, pk = id) 
    # id값이 있는 해당 데이터를 가져오거나 데이터가 없을 경우에 404에러를 띄우라는 의미
    # pk = primary key (기본키)
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





    