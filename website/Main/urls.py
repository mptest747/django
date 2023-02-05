from django.urls import path

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from . import views

urlpatterns = [
    path('',views.PostView),
    path('TOPLIST/',views.PostView, name="TOPLIST"),
    path('<slug:slug>/',views.DetailView, name="post_detail"),
    path('india/trending/',IndiaTrending.as_view(), name="IndiaTrending"),
    path('<str:parent_cat>',Parent_Cat.as_view(), name="parent_cat"),
    #path('<str:parent_cat>/<str:child_cat>/',Child_Cat.as_view(), name="child_cat"),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)