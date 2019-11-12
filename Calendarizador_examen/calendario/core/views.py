from django.shortcuts import render, HttpResponse
import requests
from django.views.generic.base import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    #return render(request,'core/home.html')
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class GrupoPageView(TemplateView):
    """ if request.method == 'GET':
            
            idNombre = ""
            idCuatri = ""

            idNombre = request.GET["idNombre"]
            idCuatri = request.GET["idCuatri"]
            
            grupos = [idCuatri]
            
    # return render(request,'core/grupos.html')"""

    template_name = "core/grupos.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
   

class AsignaturaPageView(TemplateView):
    #return render(request,'core/asignatura.html')
    template_name = "core/asignatura.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AulaPageView(TemplateView):
    #return render(request,'core/aula.html')
    template_name = "core/aula.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CalendarioPageView(TemplateView):
    #return render(request,'core/calendario.html')
    template_name = "core/calendario.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
