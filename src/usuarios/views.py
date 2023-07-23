from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm

# Create your views here.

from django.contrib import messages

def loginPage(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(request, username=username1, password=password1)

        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.add_message(request, messages.ERROR, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')

    context = {}
    return render(request, 'blog/login.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            messages.success(request, "La Cuenta se creó con Éxito")
            login(request, user)
            return redirect('blog:home')
    context = {'form':form}
    return render(request,'blog/register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('blog:home')