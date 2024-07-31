from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CamarasDB

# Create your views here.

@login_required
def index(request):
    if 'mostrar_modal_add' in request.session:
        modal_add = request.session['mostrar_modal_add']
        return render(request, 'cameras.html', {'modal_add': modal_add})
    else:     
        return render(request, 'cameras.html')

def create_cameras(request):
    camaras=CamarasDB(nombre_usuario=request.POST['usuario'], passwords=request.POST['contraseña'],
    mara=request.POST['ip'],puerto=request.POST['puerto'],ambiente_fk=request.POST['sector'])
    camaras.save()
    return redirect ('/cameras/')

def set_session_modal_add(request):
    request.session['mostrar_modal_add'] = True
    return redirect ('/cameras/')

def remove_modal(request):
    if 'mostrar_modal_add' in request.session:
        del request.session['mostrar_modal_add']
        
    return redirect ('/cameras/')







