from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('result')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('reservation')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('result')
    return render(request, 'accounts/signup.html')