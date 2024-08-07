from django.contrib import admin
from django.urls import path
from myapp import views  # Certifique-se de que as views estão importadas corretamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.entrar, name='entrar'),  # Mapeia a URL para a view de login
    path('chamados/', views.chamados, name='chamados'),
    path('sair/', views.sair, name='sair'),
]
