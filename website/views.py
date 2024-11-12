from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfull...")
            return redirect('home')
        else:
            messages.success(request, "Not valid username...")
            return redirect('home')

    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have Logged out...")
    return redirect('home')

