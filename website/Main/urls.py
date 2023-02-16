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
    path('<slug:slug>/',DetailView.as_view(), name="post_detail"),
    path('<str:category>/trending/',GetTrending.as_view(), name="GetTrending"),
    path('TOPLIST/<str:parent_cat>',Parent_Cat.as_view(), name="parent_cat"),  
    path('TOPLIST/<str:parent_cat>/<str:child_cat>',Child_cat.as_view(), name="child_cat"),      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)