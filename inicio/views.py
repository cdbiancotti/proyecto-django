from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Animal


def mi_vista(request):
    print('PASE POR ACA!!!!!')
    return HttpResponse('<h1>Mi primera vista</h1>')

# version con HttpResponse
# def mostrar_fecha(request):
#     dt = datetime.now()
#     dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
#     return HttpResponse(f'<p>{dt_formateado}</p>')

def saludar(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre} {apellido}</h1>')

def mi_primer_template(request):
    archivo = open(r'C:\Users\cdbia\Desktop\proytectos\proyecto-django\templates\mi_primer_template.html', 'r')
    # archivo = open(r'mi_primer_template.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

# version con Templates
def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    
    # archivo = open(r'C:\Users\cdbia\Desktop\proytectos\proyecto-django\templates\mi_primer_template.html', 'r')
    
    # archivo = open(r'mostrar_fecha.html', 'r')
    # template = Template(archivo.read())
    # archivo.close()
    template = loader.get_template(r'mostrar_fecha.html')
    
    datos = {'fecha': dt_formateado}
    
    # contexto = Context({'fecha': dt_formateado})
    # template_renderizado = template.render(contexto)
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)
    
def prueba_template(request):
    
    datos = {
        'nombre': 'Pepito',
        'apellido': 'Grillo',
        'edad': 14,
        'anios': [
            1995, 2004, 2014, 2017, 2021, 2022
        ]
    }
    
    template = loader.get_template(r'prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

def crear_animal(request):
    animal = Animal(nombre='Ricardito', edad=3)
    print(animal.nombre)
    print(animal.edad)
    animal.save()
    datos = {'animal': animal}
    template = loader.get_template(r'crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)
    
    