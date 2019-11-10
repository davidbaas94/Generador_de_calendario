from django.shortcuts import render, HttpResponse

# Create your views here.

def grupos(request):
    return render(request, "core/grupos.html")

def asignatura(request):
    return render(request, "core/asignatura.html")

def aula(request):
    return render(request, "core/aula.html")

def calendar(request):
    return render(request, "core/calendario.html")
