from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required    
from django.contrib.auth.models import User   
from django.contrib.auth.hashers import make_password         


from .models import Student

@login_required
def add_Fees(request):
    # info = Student.objects.ge(user=request.user)
    # context = {'info': info}
    return render(request,'index.html')

def register(request):

    if request.method == 'POST':
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        phone = request.POST.get('phone')
        roll = request.POST.get('roll')
        students = Student(fName=fName, lName=lName, roll=roll, phone=phone)
        students.save()
        context = {'roll': roll }
        return render(request, 'signup.html', context)
    return render(request, 'register.html')

def signup(request):
    if request.method=="POST":
        susername=request.POST.get('username')
        password=request.POST.get('password')
        encrypted_password = make_password(password)
        user = User(username=susername, password=encrypted_password)
        user.save() 
        return redirect('add_Fees')
    return render(request, "signup.html")
 