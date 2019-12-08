"""fonasaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import homeView
from personas.views import personasView, ninoView, jovenView, ancianoView, addNino, addJoven
from personas.views import addAnciano, delPerson, consultaView, addConsulta, delConsulta, atender
from personas.views import listaEsperaView, changeEstado, liberarConsultas, pacientesMayorRiesgo, pacientesFumadoresUrgente
from personas.views import pacienteMasAnciano, mayorConsulta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView),
    path('personas/', personasView),
    path('personas/nino/', ninoView),
    path('addNino/', addNino),
    path('delPerson/<int:person_id>/', delPerson),
    path('personas/joven/', jovenView),
    path('addJoven/', addJoven),
    path('personas/anciano/', ancianoView),
    path('addAnciano/', addAnciano),
    path('consulta/', consultaView),
    path('addConsulta/', addConsulta),
    path('delConsulta/<int:consulta_id>/', delConsulta),
    path('atender/<int:person_id>/', atender),
    path('listaEspera/', listaEsperaView),
    path('changeEstado/<int:consulta_id>/', changeEstado),
    path('liberarConsultas/', liberarConsultas),
    path('mayorRiesgo/<int:noHistoriaClinica>/', pacientesMayorRiesgo),
    path('fumadoresUrgente/', pacientesFumadoresUrgente),
    path('masAnciano/', pacienteMasAnciano),
    path('mayorConsulta/', mayorConsulta),
]
