from django.contrib import admin
from .models import Idioma, Postulante, Organizacion, Busquedalaboral, Barrio, Ciudad, Pais, Documento, Genero, Estado, Rol, BusquedaTecnologia, PostulanteBusqueda, PostulanteRol, PostulanteTecnologia, Provincia,Tecnologia, Tipoorganizacion

admin.site.register(Idioma)
admin.site.register(Postulante)
admin.site.register(Organizacion)
admin.site.register(Busquedalaboral)
admin.site.register(Barrio)
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Documento)
admin.site.register(Genero)
admin.site.register(Estado)
admin.site.register(Rol)
admin.site.register(BusquedaTecnologia)
admin.site.register(PostulanteBusqueda)

admin.site.register(PostulanteRol)
admin.site.register(PostulanteTecnologia)
admin.site.register(Provincia)
admin.site.register(Tecnologia)
admin.site.register(Tipoorganizacion)

# Register your models here.
