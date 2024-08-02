from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CamarasDB

# Create your views here.

@login_required
def index(request):
    return render(request, 'cameras.html')

def create_cameras(request):
    #camaras = CamarasDB(nombre_usuario=request.POST['usuario'], #passwords=request.POST['contraseña']
    #CAmara=request.POST['ip'],puerto=request.POST['puerto'],#ambiente_fk=request.POST['sector'])
    #camaras.save()
    return redirect ('/cameras/')

@login_required
def modal_new(request):
    return render(request, 'modal-add.html')

@login_required
def modal_remove(request):
    return render(request, 'modal-remove.html')

@login_required
def camera_detail(request, cam):
    return render(request, 'camera_detail.html', {'camera': cam})







