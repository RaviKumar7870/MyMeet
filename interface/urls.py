from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.current_meeting, name="home"),
    path('register/',views.registerPage, name="register"),

    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('newmeeting',views.newMeeting,name="newmeeting"),
    path('newmeetinglink',views.newmeetinglink,name="newmeetinglink"),
    path('deleteMeet/<str:id>',views.deleteMeet,name="deleteMeet"),
]