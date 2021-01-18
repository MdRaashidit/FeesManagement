from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required    
from django.contrib.auth.models import User   
from django.contrib.auth.hashers import make_password                

@login_required
def add_Fees(request):
    return render(request,'index.html')



def signup(request):
    if request.method=="POST":
        susername=request.POST.get('username')
        password=request.POST.get('password')
        encrypted_password = make_password(password)
        user = User(username=susername, password=encrypted_password)
        user.save() 
        return redirect('add_Fees')
    return render(request, "signup.html")
 