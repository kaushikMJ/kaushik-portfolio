from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request,"all_blogs.html",{'blogs':blogs})


def detail(request,blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request,"detail.html",{'blog':blog})