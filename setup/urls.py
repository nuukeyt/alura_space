from django.contrib import admin
from django.urls import path
from galeria.views import index
from galeria.views import imagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
