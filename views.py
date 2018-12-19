from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogPost
# Create your views here.

def index(request):

    posts = BlogPost.objects.all()[:10]
    # context = {
    #      'title': 'Latest Posts',
    #      'recent_post': posts
    #      }
    return render(request,'blogs/index.html', {'posts': posts})

 #views should now have context


def details(request, id):
    post = BlogPost.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'blogs/details.html', context)



