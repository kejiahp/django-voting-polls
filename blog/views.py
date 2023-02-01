
from django.shortcuts import get_object_or_404, render
from blog.models import Blog

def bloglist(request):
    posts = Blog.objects.filter(is_displayed=True)
    context = {
        "posts":posts
    }
    return render(request,"blog_home.html",context)

def blogdetails(request,id):
    post = get_object_or_404(Blog, slug=id)
    context = {
        "post":post
    }
    return render(request,"blog_details.html",context)