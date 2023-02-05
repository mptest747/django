from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Post
from django.views import generic ,View


def PostView(request):
    allPosts=Post.objects.filter(status=1).order_by('-created_on')[:10]
    return render(request, 'index.html', {'allPosts': allPosts})
    
def DetailView(request,slug):
  DetailView = Post.objects.get(slug=slug)
  context = {
        'DetailView': DetailView
    }
  return render(request,'post_detail.html',context)


class IndiaTrending(View):
    def get(self,request):
        allPosts = Post.objects.filter(parent_cat='India').order_by('-created_on')[:10]
        return render(request, 'index.html', {'allPosts': allPosts})

class Parent_Cat(View):
    def get(self,request,parent_cat):
        allPosts = Post.objects.filter(parent_cat=parent_cat).order_by('-created_on')[:10]
        return render(request, 'index.html', {'allPosts': allPosts})
        
# class Child_Cat(View):
#     def get(self,request,*args, **kwargs):
#         child_cat=kwargs.get('child_cat')
#         print('----------------------------------------------------------------')
#         allPosts = Post.objects.filter(child_cat=child_cat).order_by('-created_on')[:10]
#         return render(request, 'index.html', {'allPosts': allPosts})
