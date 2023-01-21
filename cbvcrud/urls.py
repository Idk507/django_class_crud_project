"""cbvcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cbvcrudapp import views
from django.views.generic.base import TemplateView
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.greetingview.as_view(greetingmsg='')),
    path('slv/',views.studentlistview.as_view(template_name='studentlist.html'),name='list'),
    path('<int:pk>/',views.studentdetailview.as_view(template_name='studentdetail.html'),name='detail'),
    path('create/',views.studentcreate.as_view(template_name='forms.html')),
    path('update/<int:pk>/',views.studentupdate.as_view(template_name='forms.html')),
    path('delete/<int:pk>/',views.studentdelete.as_view(template_name='delete.html')),
    path('',TemplateView.as_view(template_name="studentlist.html"),name="intro")
]
    
    
