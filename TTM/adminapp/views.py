from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .models import Admin, Register, Packages


def ttmhome(request):
    return render(request,"ttmhome.html")
def editpackage(request):
    return render(request, "package.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})
#def loginfail(request):
#    return render(request,"loginfail.html")

def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        #flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
        flag=Register.objects.filter(username=adminuname,password=adminpwd).values()
        if adminuname == "grkrao":
            return render(request, "adminhome.html")
        if flag:
            return render(request,"ttmhome.html")
        else:
            return render(request,"loginfail.html")
def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username taken...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request,"register.html")
def checkpackage(request):
    if request.method == "POST":
        tourcode = request.POST["tourcode"]
        tourname = request.POST["tourname"]
        tourpackage = request.POST["tourpackage"]
        desc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tourcode,tourname=tourname,tourpackage=tourpackage,desc=desc)
        pack.save()
        messages.info(request, "Data Inserted Successfully...")
        return render(request, "adminhome.html")


def checkchangepasswd(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        #flag=Admin.objects.filter(Q(username=uname)&Q(password=adminpwd))
        flag=Register.objects.filter(username=uname,password=opwd).values()

        if flag:
            Register.objects.filter(username=uname, password=opwd).update(password=npwd)
            messages.info(request, "Password Change Successfully...")
            return render(request,"index.html")
        else:
            messages.info(request, "Password Change Successfully...")
            return render(request, "changepassword.html")