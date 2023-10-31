from django.shortcuts import render,redirect
 
from django.contrib import messages
from store.forms import CustomUserform,LoginForm
from django.contrib.auth import login,user_logged_out,logout


def register(request):
    form = CustomUserform()
    if request.method == 'POST':
        form = CustomUserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'register suceessfully')
            return redirect('loginpage')  # Redirect to login page after successful registration
    else:
        form = CustomUserform()
    return render(request, 'store/register.html', {'form': form})


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"YOu are already logged in")
        return redirect('/')
    else:
     if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"Logged in successfully")
            # Redirect to a success page or perform further actions
            return redirect('/')
        else:
           messages.error(request,"Invalid Username or password")
           
     else:
        form = LoginForm()
        

    return render(request, 'store/login.html', {'form': form})


def logoutpage(request):
    if request.user.is_authenticated:
     logout(request)
     messages.success(request,"logged out successfully")
    return redirect('/')