from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm

# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        # nombre_usuario = form.cleaned_data.get('username')
        # contra = form.cleaned_data.get('password')

        user = authenticate(request, username=username1,password=password1)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
         messages.info(request, 'Usuario o contraseña es incorrecto')   
    context = {}
    return render(request,'login.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " La Cuenta se creo con Exito")
            return redirect('index')
    context = {'form':form}
    return render(request,'register.html',context)
