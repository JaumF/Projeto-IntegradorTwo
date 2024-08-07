from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def entrar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario_aux = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
            return redirect('entrar')  # Redireciona para a página de login

        usuario = authenticate(username=usuario_aux.username, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('home')  # Redireciona para a página inicial após login

        messages.error(request, 'Senha incorreta.')
        return redirect('entrar')  # Redireciona para a página de login se a autenticação falhar

    # GET request: renderiza o template de login
    return render(request, 'login.html')
