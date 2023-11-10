from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = POST.get('nome')
    idade = request.POST.get('idade')
    novo_usuario.save()
    # exobir todos os usuarios ja cadastrados em uma nava pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # retornar os dados para a paginad e listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)