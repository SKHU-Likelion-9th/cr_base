from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

