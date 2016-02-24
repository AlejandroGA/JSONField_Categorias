from django.shortcuts import render
from inmuebles.models import *
from .forms import *
from django.http import HttpResponseRedirect


def servicios(request):
    if request.POST:
        Servicios.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'servicios.html',)






def belleza(request):
    if request.POST:
        Belleza.objects.create(
            titulo = request.POST['titulo'],
            foto1 = request.POST['foto1'],
            datos = {'precio': request.POST['precio']}
        )
        form = fotos(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/belleza/')
    else:
        form = fotos()
    return render(request, 'belleza.html', {'form':form})

def clases(request):
    if request.POST:
        Clases.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'clases.html',)

def fiestas(request):
    if request.POST:
        Fiestas.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'fiestas.html',)

def hogar(request):
    if request.POST:
        Hogar.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'hogar.html',)

def mantenimiento(request):
    if request.POST:
        Mantenimiento.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'mantenimiento.html',)

def mascotas(request):
    if request.POST:
        Mascotas.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'mascotas.html',)

def otros(request):
    if request.POST:
        Otros.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'otros.html',)

def profesionales(request):
    if request.POST:
        Profesionales.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'profesionales.html',)

def recreacion(request):
    if request.POST:
        Recreacion.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'recreacion.html',)

def reparacion(request):
    if request.POST:
        Reparacion.objects.create(
            titulo = request.POST['titulo'],
            datos = {'precio': request.POST['precio']}
        )
    return render(request, 'reparacion.html',)



