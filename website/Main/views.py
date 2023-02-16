from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.views import generic ,View
from django.core.paginator import Paginator



def PostView(request):
    allPosts=Post.objects.filter(status=2).order_by('-created_on')[:10]
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
    ]
    return render(request, 'index.html', {'allPosts': allPosts ,'breadcrumbs':breadcrumbs})


class DetailView(View):
    def get(self,request,slug):
        DetailView = Post.objects.get(slug=slug)
        context = {
                'DetailView': DetailView
            }
        return render(request,'post_detail.html',context)

class GetTrending(View):
    def get(self,request,category):
        allPosts = Post.objects.filter(status=2).filter(parent_cat=category).order_by('-created_on')[:10]
        return render(request, 'index.html', {'allPosts': allPosts})


class Parent_Cat(View):
    def get(self,request,parent_cat):
        allPosts = Post.objects.filter(parent_cat=parent_cat).order_by('-created_on')[:10]
        return render(request, 'index.html', {'allPosts': allPosts})

class Child_cat(View):
    def get(self,request,parent_cat,child_cat):
        allPosts = Post.objects.filter(child_cat=child_cat).order_by('-created_on')[:10]
        return render(request, 'index.html', {'allPosts': allPosts})
        
