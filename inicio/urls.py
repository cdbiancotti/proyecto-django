from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('mostrar-fecha/', views.mostrar_fecha, name='mostrar_fecha'),
    path('saludar/<str:nombre>/<str:apellido>/', views.saludar, name='saludar'),
    path('mi-primer-template/', views.mi_primer_template, name='mi_primer_template'),
    path('prueba-template/', views.prueba_template, name='prueba_template'),
    path('prueba-render/', views.prueba_render, name='prueba_render'),
    
    # Animales con vistas
    # path('animales/', views.lista_animales, name='listar_animales'),
    # path('animales/crear/', views.crear_animal, name='crear_animal'),
    # path('animales/<int:id_animal>/', views.mostrar_animal, name='mostrar_animal'),
    # path('animales/<int:id_animal>/eliminar/', views.eliminar_animal, name='eliminar_animal'),
    # path('animales/<int:id_animal>/modificar/', views.modificar_animal, name='modificar_animal'),
    
    # Animales con CBV
    path('animales/', views.ListaAnimales.as_view(), name='listar_animales'),
    path('animales/crear/', views.CrearAnimal.as_view(), name='crear_animal'),
    path('animales/<int:pk>/', views.MostrarAnimal.as_view(), name='mostrar_animal'),
    path('animales/<int:pk>/eliminar/', views.EliminarAnimal.as_view(), name='eliminar_animal'),
    path('animales/<int:pk>/modificar/', views.ModificarAnimal.as_view(), name='modificar_animal'),
]
