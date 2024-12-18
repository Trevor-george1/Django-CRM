from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):

    records = Record.objects.all()



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

    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have Logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # AAUTHENTICATE 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        # lookup record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)

        delete_it.delete()
        messages.success(request, "Record deleted successful")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
