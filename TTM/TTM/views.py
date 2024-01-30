from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"login.html")
def registrationPage(request):
    return render(request,"register.html")
def contactPage(request):
    return render(request,"contact.html")
def aboutPage(request):
    return render(request,"about.html")
def changepasswordpage(request):
    return render(request,"changepassword.html")

