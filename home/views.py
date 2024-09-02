from django.shortcuts import render,redirect,get_object_or_404
from .models import Song,Topsongs,Rating
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg


# Create your views here.
@login_required(login_url='login')
def index(request):
    song  =Song.objects.all()[:3]
    topsong = Topsongs.objects.all()[3:6]
    return render(request,'index.html',{'song':song ,'topsong': topsong})

def songs(request):
    song=Song.objects.all()
    return render(request,'songs.html',{'song':song})

def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html',{'song':song})

def topsongs(request):
    topsong = Topsongs.objects.all()
    return render(request, "topsongs.html", {'topsong': topsong})

def songdetail(request,id):
    topsong=Topsongs.objects.filter(song_id=id).first()
    return render(request,'songdetail.html',{'topsong':topsong})


def Login(request):

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"User not found")
            
           
    return render(request,'login.html')

def Signup(request):

    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password =request.POST.get('confirm_password')


        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect('signup')


        if password!=confirm_password:
            messages.error(request,"Password doe not match")
            return redirect('signup')
        else:
            user =User.objects.create_user(username=username,email=email,password=password)
            user.save()

            return redirect('home')

    
    return render(request,'signup.html')

def LogOut(request):
    logout(request)
    return redirect('login')


def binary_Search(query,sorted_list):
    left=0
    right=len(sorted_list)-1
    result =[]

    while left<=right:
        mid =(left+right)//2
        mid_value =sorted_list[mid].name.lower()

        if mid_value.startswith(query.lower()):
            result.append(sorted_list[mid])
            l=mid-1
            while l>=left and sorted_list[l].name.lower().startswith(query.lower()):
                result.append(sorted_list[l])
                l=l-1
            r=mid+1
            while r<=right and sorted_list[r].name.lower().startswith(query.lower()):
                result.append(sorted_list[r])
                r=r+1

            break
        elif mid_value<query.lower():
            left=mid+1
        else:
            right=mid-1

    return result



# hello
def search(request):
    query =request.GET.get('q')
    song_results =[]
    topsong_results=[]


    if  query:
        song =Song.objects.filter(Q(name__icontains=query)).order_by('name')
        song_list=list(song)
        song_results =binary_Search(query,song_list)


        topsong=Topsongs.objects.filter(Q(name__icontains=query)).order_by('name')
        topsong_list =list(topsong)
        topsong_results=binary_Search(query,topsong_list)

    else:
        song=Song.objects.all()
        topsong=Topsongs.objects.all()

    return render(request,'search.html',{'song':song_results,'topsong':topsong_results,'query':query})
