from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from . models import Product,Cart
import math
import pandas as pd
from user.models import Favs


# Create your views here.
def price(request,id1,id2):
    if request.method == "POST":
        x = request.POST.get("hakan")
        x= list(x.split(","))
        if len(x) == 2:
            value_min = int(x[0])
            value_max = int(x[1])
            return redirect(reverse("price",kwargs={"id1":value_min,"id2":value_max}))
    product = Product.objects.filter(price__gt=id1,price__lt=id2)
    favs=list()
    carts=list()
    product=product[:48]
    if (str(request.user)) != "AnonymousUser":
        fav = Favs.objects.filter(user=request.user)
        for i in fav:
            favs.append(i.fav_product.id)
        cart = Cart.objects.filter(user=request.user)
        for i in cart:
            carts.append(i.cart_product.id)
    return render(request,"index.html",{"product":product,"favs":favs,"carts":carts})

def index(request):
    if request.method == "POST":
        x = request.POST.get("hakan")
        x= list(x.split(","))
        if len(x) == 2:
            value_min = int(x[0])
            value_max = int(x[1])

            return redirect(reverse("price",kwargs={"id1":value_min,"id2":value_max}))
    x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))

    favs=list()
    carts=list()
    product=Product.objects.all()
    product=product[:48]
    if (str(request.user)) != "AnonymousUser":
        fav = Favs.objects.filter(user=request.user)
        for i in fav:
            favs.append(i.fav_product.id)
        cart = Cart.objects.filter(user=request.user)
        for i in cart:
            carts.append(i.cart_product.id)
    return render(request,"index.html",{"product":product,"favs":favs,"carts":carts,"brand":brand})

def category_men(request,category_men,page):
    favs=list()
    carts=list()
    men_cat = Product.objects.filter(category=category_men,sex_category="Erkek")
    x=math.ceil(len(men_cat)/9)
    if page > x:
        return redirect("error")
    men_cat=(men_cat[9*(page-1):(9*page)])
    page_list=list()
    for i in range(x):
        page_list.append(i+1)
    cat=men_cat[0].category
    sex = men_cat[0].sex_category
    x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))
    if (str(request.user)) != "AnonymousUser":
        fav = Favs.objects.filter(user=request.user)
        for i in fav:
            favs.append(i.fav_product.id)
        cart = Cart.objects.filter(user=request.user)
        for i in cart:
            carts.append(i.cart_product.id)
    return render(request,"category.html",{"men_cat":men_cat,"page_list":page_list,"cat":cat,"sex":sex,"favs":favs,"carts":carts,"brand":brand})

def category_women(request,category_women,page):
    favs=list()
    carts=list()
    men_cat = Product.objects.filter(category=category_women,sex_category="Kadın")
    x=math.ceil(len(men_cat)/9)
    if page > x:
        return redirect("error")
    men_cat=(men_cat[9*(page-1):(9*page)])
    page_list=list()
    for i in range(x):
        page_list.append(i+1)
    cat=men_cat[0].category
    sex = men_cat[0].sex_category
    x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))
    if (str(request.user)) != "AnonymousUser":
        fav = Favs.objects.filter(user=request.user)
        for i in fav:
            favs.append(i.fav_product.id)
        cart = Cart.objects.filter(user=request.user)
        for i in cart:
            carts.append(i.cart_product.id)
    return render(request,"category.html",{"men_cat":men_cat,"page_list":page_list,"cat":cat,"sex":sex,"favs":favs,"carts":carts,"brand":brand})

def bag(request,page):
    favs=list()
    carts=list()
    bags = Product.objects.filter(category="Canta*Aksesuar")
    x=math.ceil(len(bags)/9)
    if page > x:
        return redirect("error")
    bags=(bags[9*(page-1):(9*page)])
    page_list=list()
    for i in range(x):
        page_list.append(i+1)
    x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))
    if (str(request.user)) != "AnonymousUser":
        fav = Favs.objects.filter(user=request.user)
        for i in fav:
            favs.append(i.fav_product.id)
        cart = Cart.objects.filter(user=request.user)
        for i in cart:
            carts.append(i.cart_product.id)
    return render(request,"bag.html",{"bags":bags,"page_list":page_list,"favs":favs,"carts":carts,"brand":brand})
     
def detail(request,id):
    product = Product.objects.filter(id=id).first()
    if request.method == "POST":
        if (str(request.user)) != "AnonymousUser":
            stars=request.POST.get("keyword")
            cart_number = request.POST.get("cart_number")
            if stars != None:
                rating = Product.objects.filter(id=id).first()
                rating_new = rating.rating
                rating_new.update({request.user.username:stars})
                rating.rating=rating_new
                rating.save()
                messages.warning(request,"puanınız başarıyla kaydedilmiştir")
                return redirect(reverse("product:details",kwargs={"id":id}))
            else:
                cart = Cart.objects.filter(user=request.user,cart_product=id).first()
                if cart is None:
                    new_fav = Cart(user=request.user,cart_product=product,number=cart_number)
                    new_fav.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.info(request,"Bu ürün sepetinizde bulunmaktadır!!")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request,"Lütfen giriş yapınız!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    if product.rating != "":
        rating_new=product.rating
        rat=pd.Series(rating_new)
        rat=pd.to_numeric(rat,errors="coerce")
        rat=rat.mean()
        rat=round(rat,1)
        rating = Product.objects.filter(id=id).first()
        rating.rating_total=rat
        rating.save()
        favs=list()
        if (str(request.user)) != "AnonymousUser":
            fav = Favs.objects.filter(user=request.user)
            for i in fav:
                favs.append(i.fav_product.id)
    x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))
    return render(request,"details.html",{"product":product,"rat":rat,"favs":favs,"brand":brand})

@login_required(login_url="error")
def fav(request):
    favs = Favs.objects.filter(user=request.user)
    fav = list()
    carts = list()
    for i in favs:
        fav.append(i.fav_product) 
    cart = Cart.objects.filter(user=request.user)
    for i in cart:
        carts.append(i.cart_product.id)
        x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))
    return render(request,"favourite.html",{"fav":fav,"carts":carts,"brand":brand})

def brands(request,name,page):
    favs=list()
    carts=list()
    product =Product.objects.filter(marka=name)
    x=math.ceil(len(product)/9)
    if page > x:
        return redirect("error")
    product=(product[9*(page-1):(9*page)])
    page_list=list()
    for i in range(x):
        page_list.append(i+1)
    cat=product[0].marka
    x=list()
    marka = Product.objects.all()
    for i in marka:
        x.append(i.marka)
    data = pd.DataFrame({"marka":x,"sayi":[1 for i in range(len(marka))]},range(len(marka)))
    data = data.groupby("marka").count()
    marka = list(data.index.values)
    sayi = list(data["sayi"])
    brand = list(zip(marka,sayi))
    if (str(request.user)) != "AnonymousUser":
        fav = Favs.objects.filter(user=request.user)
        for i in fav:
            favs.append(i.fav_product.id)
        cart = Cart.objects.filter(user=request.user)
        for i in cart:
            carts.append(i.cart_product.id)
    
    return render(request,"brands.html",{"product":product,"page_list":page_list,"cat":cat,"favs":favs,"carts":carts,"brand":brand})
@login_required(login_url="error")
def addfav(request,id):
    product = get_object_or_404(Product,id=id)
    new_fav = Favs(user=request.user,fav_product=product)
    new_fav.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="error")
def deletefav(request,id):
    fav = get_object_or_404(Favs,fav_product=id,user=request.user)
    fav.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="error")
def cart(request):
    total=0
    if request.method == "POST":
        quantity = request.POST.get("quantity")
        id =request.POST.get("id")
        product = Cart.objects.filter(cart_product=id).first()
        product.number = quantity
        product.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    cart_detail=Cart.objects.filter(user=request.user)
    for cart in cart_detail:
        total+=(cart.number * cart.cart_product.price)
    return render(request,"cart.html",{"cart_detail":cart_detail,"total":total})

@login_required(login_url="error")
def addcart(request,id):
    product = get_object_or_404(Product,id=id)
    cart = Cart.objects.filter(cart_product=id,user=request.user).first()
    if cart is None:
        new_fav = Cart(user=request.user,cart_product=product)
        new_fav.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.info(request,"Bu ürün sepetiniz bulunmaktadır!")
        return redirect("index")      

@login_required(login_url="error")
def deletecart(request,id):
    cart = get_object_or_404(Cart,cart_product=id,user=request.user)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def error(request):
    return render(request,"404.html")

def Contact(request):
    return render(request,"harita.html")
