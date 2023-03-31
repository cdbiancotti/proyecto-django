from django.contrib import admin
from inicio.models import Animal, Persona

# Register your models here.

# v1
# admin.site.register(Animal)
# admin.site.register(Persona)

# v2
admin.site.register([Persona, Animal])