from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Person, Nino, Joven, Anciano, Consulta
from itertools import chain

# Create your views here.
def personasView(request):
    all_people = list(chain(Nino.objects.filter(consulta=None), Joven.objects.filter(consulta=None), Anciano.objects.filter(consulta=None)))
    all_people = sorted(all_people, key=lambda x: x.prioridad())
    return render(request, 'personas.html', {'all_people': all_people})

def ninoView(request):
    return render(request, 'nino.html')

def addNino(request):
    nombre = request.POST['nombre']
    edad = request.POST['edad']
    noHistoriaClinica = request.POST['noHistoriaClinica']
    peso = request.POST['peso']
    estatura = request.POST['estatura']

    new_nino = Nino(nombre=nombre, edad=edad, noHistoriaClinica=noHistoriaClinica, peso=peso, estatura=estatura, listaEspera=False)
    new_nino.save()

    return HttpResponseRedirect('/personas/')

def jovenView(request):
    return render(request, 'joven.html')

def addJoven(request):
    nombre = request.POST['nombre']
    edad = request.POST['edad']

    noHistoriaClinica = request.POST['noHistoriaClinica']
    if 'fumador' in request.POST:
        fumador = True 
    else:
        fumador = False
    
    anos_fumando = request.POST['anos_fumando']

    if anos_fumando == '':
        anos_fumando = 0

    new_joven = Joven(nombre=nombre, edad=edad, noHistoriaClinica=noHistoriaClinica, fumador=fumador, anos_fumando=anos_fumando, listaEspera=False)
    new_joven.save()

    return HttpResponseRedirect('/personas/')

def ancianoView(request):
    return render(request, 'anciano.html')

def addAnciano(request):
    nombre = request.POST['nombre']
    edad = request.POST['edad']
    noHistoriaClinica = request.POST['noHistoriaClinica']

    if 'tieneDieta' in request.POST:
        tieneDieta = True 
    else:
        tieneDieta = False

    new_anciano = Anciano(nombre=nombre, edad=edad, noHistoriaClinica=noHistoriaClinica, tieneDieta=tieneDieta, listaEspera=False)
    new_anciano.save()

    return HttpResponseRedirect('/personas/')

def delPerson(request, person_id):
    item_to_delete = Person.objects.get(id=person_id)
    item_to_delete.delete()

    return HttpResponseRedirect('/personas/')

def atender(request, person_id):
    all_people = list(chain(Nino.objects.all(), Joven.objects.all(), Anciano.objects.all()))
    persona_atender = [i for i in all_people if i.id == person_id][0]

    prioridad = persona_atender.prioridad()

    atender_en = 'CGI'

    if prioridad > 4:
        atender_en = 'URGENCIA'
    elif isinstance(persona_atender, Nino):
        if prioridad <= 4:
            atender_en = 'PEDIATRIA'

    consultaDisp = Consulta.objects.filter(tipoConsulta=atender_en, estado=True)

    if consultaDisp:
        persona_atender.consulta = consultaDisp[0]
        persona_atender.listaEspera = False
        consultaDisp[0].cantidadPersonas += 1
        consultaDisp[0].save()
    else:
        persona_atender.listaEspera = True
    
    persona_atender.save()

    return HttpResponseRedirect('/personas/')

def consultaView(request):
    all_consultas = Consulta.objects.all()
    return render(request, 'consultas.html', {"all_consultas": all_consultas})

def addConsulta(request):
    idConsulta = request.POST['idConsulta']
    cantidadPersonas = request.POST['cantidadPersonas']
    nombreEspecialista = request.POST['nombreEspecialista']
    tipoConsulta = request.POST['tipoConsulta']
    estado = request.POST['estado']

    if estado == 'INACTIVA':
        estado = False
    else:
        estado = True

    new_consulta = Consulta(idConsulta=idConsulta, cantidadPersonas=cantidadPersonas, nombreEspecialista=nombreEspecialista, tipoConsulta=tipoConsulta, estado=estado)
    new_consulta.save()

    return HttpResponseRedirect('/consulta/')

def delConsulta(request, consulta_id):
    item_to_delete = Consulta.objects.get(id=consulta_id)
    item_to_delete.delete()

    return HttpResponseRedirect('/consulta/')

def listaEsperaView(request):
    all_people = Person.objects.filter(listaEspera=1)
    return render(request, 'listaDeEspera.html', {'all_people': all_people})

def changeEstado(request, consulta_id):
    item_to_change = Consulta.objects.get(id=consulta_id)
    item_to_change.estado = not item_to_change.estado
    item_to_change.save()

    return HttpResponseRedirect('/consulta/')

def liberarConsultas(request):
    consultas = Consulta.objects.filter(estado=0)
    for c in consultas:
        c.estado = 1
        c.save()
    
    all_people = Person.objects.filter(listaEspera=1)
    for p in all_people:
        atender(None, p.id)

    return HttpResponseRedirect('/consulta/')

def pacientesMayorRiesgo(request, noHistoriaClinica):
    all_people = list(chain(Nino.objects.all(), Joven.objects.all(), Anciano.objects.all()))
    personOfInterest = [i for i in all_people if i.noHistoriaClinica == noHistoriaClinica][0]

    all_people = [p for p in all_people if p.prioridad() < personOfInterest.prioridad()]

    return render(request, 'mayorRiesgo.html', {'all_people': all_people})

def pacientesFumadoresUrgente(request):
    fumadores = Joven.objects.filter(fumador=1)
    fumadores_urgente = [f for f in fumadores if f.prioridad() > 4]

    return render(request, 'fumadoresUrgente.html', {'all_people': fumadores_urgente})

def pacienteMasAnciano(request):
    old = Anciano.objects.all()
    older = max(old, key=lambda x: x.edad)
    html = "<h1>Nombre: {} | Edad: {}</h1>".format(older.nombre, older.edad)
    return HttpResponse(html)

def mayorConsulta(request):
    consultas = Consulta.objects.all()
    consulta_max = max(consultas, key=lambda x: x.cantidadPersonas)
    html = "<h1>Tipo: {} | Cantidad de personas: {}</h1>".format(consulta_max.tipoConsulta, consulta_max.cantidadPersonas)
    return HttpResponse(html)
