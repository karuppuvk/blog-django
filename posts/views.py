from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/posts_page.html', {'post': post})

@login_required(login_url="/users/login/")
def post_new(request):
    if  request.method == "POST":
        form=forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            #save with user
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return redirect('posts:list')

    else:
        form=forms.CreatePost()
    return render(request,'posts/post_new.html',{'form':form})