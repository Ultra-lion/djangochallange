from django.shortcuts import render
from django.http import HttpResponse
from challangeapp.models import Topic,AccessRecord,Webpage
from . import forms
from challangeapp.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import  login_required
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# from challangeapp.forms import NewUser

# Create your views here.

def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request,'challangeapp/index.html',context_dict)

def other(request):
    return render(request,'challangeapp/other.html')

def relative(request):
    return render(request,'challangeapp/relative_url_templates.html')


# def user_index(request):
#     # Webpage_list = AccessRecord.objects.order_by('date')
#     user_list = User.objects.order_by('age')
#     user_dict = {'user_records':user_list}
#     return render(request,'challangeapp/user_index.html',context=user_dict)
#
# def users(request):
#     form = NewUser()
#
#     if request.method == 'POST':
#         form = NewUser(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("invalid form")
#
#     return render(request,'challangeapp/user_form.html',{'form':form})


def ditto(request):
    return HttpResponse("<p> This is a test paragraph</p>")

def imgsho(request):
    return render(request,'challangeapp/image.html')


def register(request):
    registered = False
    # user_form = UserForm()
    # profile_form = UserProfileInfoForm()

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'challangeapp/registration.html',{'user_form':user_form,
                                                        'profile_form':profile_form,

                                            'registered':registered})



def formreq(request):
    form = forms.FormName()
    print("requested")
    if request.method == 'POST' :
        print("posted")
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation success")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])



    return render(request,'challangeapp/form_page.html',{'form':form})



def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login but failed ")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("invalid login details provided")
    else:
        return render(request,'challangeapp/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
