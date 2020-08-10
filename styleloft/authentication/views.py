from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import client
# Create your views here.


def user_login(request):
    if request.method == 'GET':

        return render(request, 'login.html', {'pass': 'ok'})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('add_product')
            else:
                return redirect('/')
        else:
            return render(request, 'login.html', {'pass': 'fail'})


def user_signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'], first_name=request.POST['fname'], last_name=request.POST['lname'])
        user.save()
        return redirect('/login')


def user_logout(request):
    logout(request)
    return redirect('/')
