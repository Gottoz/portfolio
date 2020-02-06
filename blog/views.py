from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    posts = Blog.objects
    return render(request, 'blog/allposts.html', {'posts': posts})


def postdetail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})

