from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def plogin(request):

    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return  redirect('registration')
                print('Что-то не так')
    form = LoginForm()
    context = {'login_form':form}
    return render(request, "profiles/login.html", context)



@login_required()
def home(request):
    return render(request, "profiles/home.html")


def logoutuser(request):
    logout(request)
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password == password2:
                user = authenticate(request, username = username, password=password)
                if user is not None:
                    print('ТАкой пользователь уже есть')
                    form = RegistrationForm()
                    context = {'reg_form': form}
                    return render(request, "profiles/registration.html", context)
                else:
                    newuser = User.objects.create_user(username = username, password=password)
                    newuser.save()
                    return redirect('plogin')
            else:
                print('Пароли не совпадают')
                form = RegistrationForm()
                context = {'reg_form': form}
                return render(request, "profiles/registration.html", context)
