from django.urls import path
from .views import HomePageView, GrupoPageView, AsignaturaPageView, AulaPageView, CalendarioPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('grupo/', GrupoPageView.as_view(), name="grupo"),
    path('asignatura/', AsignaturaPageView.as_view(), name="asignatura"),
    path('aula/', AulaPageView.as_view(), name="aula"),
    path('calendario/', CalendarioPageView.as_view(), name="calendario"),
]
