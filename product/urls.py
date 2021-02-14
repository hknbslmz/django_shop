from django.contrib import admin
from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('men/<str:category_men>/<int:page>',views.category_men,name="category_men"),
    path('women/<str:category_women>/<int:page>',views.category_women,name="category_women"),
    path('<int:id>/',views.detail,name="details"),
    path('fav/add/<int:id>/',views.addfav,name="addfav"),
    path('fav/',views.fav,name="favs"),
    path('fav/delete/<int:id>/',views.deletefav,name="deletefav"),
    path('cart/add/<int:id>/',views.addcart,name="addcart"),
    path('cart/',views.cart,name="carts"),
    path('cart/delete/<int:id>',views.deletecart,name="deletecart"),
    path('bags&accessory/<int:page>/',views.bag,name="bags"),
    path('brand/<str:name>/<int:page>/',views.brands,name="brand"),
    
    

    

]