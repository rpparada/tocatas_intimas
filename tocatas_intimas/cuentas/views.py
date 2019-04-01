from django.shortcuts import render, redirect

# Create your views here.
def ingresar(request):
    return render(request,'cuentas/iniciar_sesion.html')

def registrar(request):
    return render(request,'cuentas/registrar.html')

def salir(request):
    return redirect('index')

def micuenta(request):
    return render(request,'cuentas/micuenta.html')
