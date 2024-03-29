"""challangeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from challangeapp import views
# from challangeapp2 import views

urlpatterns = [
    # re_path(r'^$',views.index,name='index'),
    path('',views.index,name='index'),
    # url(r'^$',views.index,name='index'),
    path('challangeapp/',include('challangeapp.urls')),
    path('logout',views.user_logout,name='logout'),
    # url(r'^challangeapp2/',include('challangeapp2.urls')),
    # path('ditto',views.ditto,name='ditto'),
    path('admin/', admin.site.urls),
]
