from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User

# Create your views here.
def ingresar_registrar(request):

    if 'botoningresa' in request.POST:
        if request.method == 'POST':
            email = request.POST['Email Login']
            contra = request.POST['Password Login']
            print(email)
            print(contra)
            user = auth.authenticate(username=email, password=contra)

            if user is not None:
                auth.login(request, user)
                messages.success(request,'Ingreso exitoso')
                return redirect('micuenta')
            else:
                messages.error(request,'Usuario y/o contraseña invalidos')
                return redirect('ingresar_registrar')
        else:
            return render(request,'cuentas/ingresar_registrar.html')

    if 'botoncrea' in request.POST:
        if request.method == 'POST':
            nombre_completo = request.POST['Full Name Register']
            nombre_usuario = request.POST['Username Register']
            contra = request.POST['Password Register']
            contra2 = request.POST['Re-Password Register']
            email = request.POST['Email Register']

            # verifinado contraseñas
            if contra == contra2:
                # verifinado nombre usuario
                if User.objects.filter(username=nombre_usuario).exists():
                    messages.error(request,'Nombre de usuario ya registrado, prueba con otro')
                    return redirect('ingresar_registrar')
                else:
                    # vefifica email
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'Email ya registrado, prueba con otro')
                        return redirect('ingresar_registrar')
                    else:
                        # Todo ok
                        user = User.objects.create_user(username=email,email=email,password=contra)
                        user.save()
                        messages.success(request,'Usuario creado, ya puedes ingresar')
                        return redirect('ingresar_registrar')
            else:
                messages.error(request,'Contraseñas no son iguales')
                return redirect('ingresar_registrar')
        else:
            return render(request,'cuentas/ingresar_registrar.html')

    return render(request,'cuentas/ingresar_registrar.html')

def salir(request):
    return redirect('index')

def micuenta(request):
    return render(request,'cuentas/micuenta.html')
