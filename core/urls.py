from django.urls import path
from .import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('postulantes', views.postulantes, name='postulantes'),
    path('postulantes/crear', views.crear, name='crear'),
    path('postulantes/editar/<int:id>', views.editar, name='editar'),
    path('postulantes/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar' ),
    path('postulantes/idioma/<int:id>', views.idioma, name='idioma'),
    
    
]