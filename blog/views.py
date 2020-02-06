from django.shortcuts import render
from .models import Blog


def allblogs(request):
    posts = Blog.objects

    return render(request, 'blog/allposts.html', {'posts': posts})
