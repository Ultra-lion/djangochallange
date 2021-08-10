from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from challangeapp import views

app_name = 'challangeapp'

urlpatterns = [
    # re_path(r'^$',views.index,name='index'),
    # path('',views.index,name='index'),
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('other',views.other,name='other'),
    path('relative',views.relative,name='relative'),
    path('ditto',views.ditto,name='ditto'),
    # path('users',views.users,name='users'),
    # path('user_index',views.user_index,name='user_index'),
    path('images',views.imgsho,name='imgsho'),
    path('register',views.register,name='register'),
    path('form',views.formreq,name='form'),
    path('logout',views.user_logout,name='logout'),
    path('login',views.user_login,name='login')
]
