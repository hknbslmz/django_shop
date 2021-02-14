from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .forms import RegisterForm,LoginForm,İnfoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from product.models import Product
from django.contrib.auth.decorators import login_required
from .models import İnfos,Favs

# Create your views here.
def RegisterORLogin(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        form2 = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            users = User.objects.filter(username=username).first()
            if users is None:
                newUser = User(username=username)
                newUser.set_password(password)
                newUser.save()
                login(request,newUser)
                messages.success(request,"Başarıyla Kayıt Oldunuz...")
                return redirect("index")
            else:
                messages.info(request,"Bu kullanıcı adı kullanılmıştır!") 
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            
            if form2.is_valid():
                username =form2.cleaned_data.get("username")
                password =form2.cleaned_data.get("password")
               
                user = authenticate(username=username,password=password)
                if user is None:
                    pass
                else:
                    login(request,user)
                    messages.success(request,"hoşgeldiniz, sayın "+str(request.user.username))
                    return redirect("index")
    if request.user.username:
        return render(request,"404.html")
    else:
        form = RegisterForm()
        form2 = LoginForm()
        return render(request,"login.html",{"form":form,"form2":form2})

@login_required(login_url="error")
def Logout(request):
    logout(request)
    messages.success(request,"çıkış yapıldı, yine bekleriz :)")
    return redirect("index")

@login_required(login_url="error")
def Addİnfo(request):
    info = İnfos.objects.all()
    form = İnfoForm(request.POST or None)
    if form.is_valid():
        adress_name = form.cleaned_data.get("adress_name")
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        adress = form.cleaned_data.get("adress")  
        tel_no = form.cleaned_data.get("tel_no")  
        email = form.cleaned_data.get("email")  
        country = form.cleaned_data.get("country")  
        city = form.cleaned_data.get("city")  
        post_code = form.cleaned_data.get("post_code")
        new_info =İnfos(user=request.user,adress_name=adress_name, name=name,surname=surname,adress=adress,tel_no=tel_no,e_mail=email,country=country,city=city,post_code=post_code)
        new_info.save()
        messages.success(request,"Adres başarıyla kayedildi.")
        return redirect("user:info")      
    return render(request,"AddAdress.html",{"form":form}) 

@login_required(login_url="error")
def İnfo(request):
    info = İnfos.objects.filter(user=request.user.id)
    return render(request,"info.html",{"info":info})

@login_required(login_url="error")
def Deleteİnfo(request,id):
    info = İnfos.objects.filter(id=id).first()
    info.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="error")
def UserDelete(request):
    user = User.objects.filter(username=request.user).first()
    user.delete()
    messages.success(request,"Hesabınız başarıyla silinmiştir, En kısa zamanda yine bekleriz :)")
    return redirect("index")




  
  

