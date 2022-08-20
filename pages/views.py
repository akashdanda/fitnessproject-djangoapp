
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout 
from .forms import UserCreationForm 

def inside(request, *args,**kwargs):
    print('hi')
    return render(request,"inside.html",{})

def loginpage(request, *args, **kwargs):
    page = 'login'
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request, "login.html",{'page':page})
def logoutUser(request, *args, **kwargs):
    logout(request)
    return redirect('login')
def registerUser(request, *args, **kwargs):
    page='register'
    form=UserCreationForm()
    
    return render(request,"login.html",{'form':form,'page':page})
# Create your views here.
def homepage(request, *args, **kwargs):

    return render(request, "firstpage.html",{})
