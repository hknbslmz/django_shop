from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('register/',views.RegisterORLogin,name="register"),
    path('logout/',views.Logout,name="logout"),
    path('add/adress/',views.Addİnfo,name="addadress"),
    path('info/',views.İnfo,name="info"),
    path('delete/adress/<int:id>',views.Deleteİnfo,name="deletadress"),
    path('delete/',views.UserDelete,name="userdelete"),





]