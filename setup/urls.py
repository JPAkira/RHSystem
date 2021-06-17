from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('', include('empresa.urls')),
    path('', include('candidato.urls')),
    path('', include('vagas.urls')),
    path('admin/', admin.site.urls),
]
