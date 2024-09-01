from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    
    path('',views.index,name="home"),
    path('songs/',views.songs,name="songs"),
    path('songs/<int:id>',views.songpost,name="songpost"),
    path('topsongs/',views.topsongs,name="topsongs"),
    path('topsongs/<int:id>',views.songdetail,name="songdetail"),
    path('login/',views.Login,name="login"),
    path('signup/',views.Signup,name="signup"),
    path('logout/',views.LogOut,name="logout"),
    path('serach/',views.search,name="search")

]
