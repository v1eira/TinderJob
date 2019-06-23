from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from ..models import VagaEmprego, Cidade, Estado


def vagas_list(request):
    vagas = Cidade.objects.all()
    print(Estado.objects.filter(nome__contains='Espírito Santo'))
    return render(request, 'jobTinder/vagas_list.html', {'vagas': vagas})


def login_user(request):
    return render(request, 'jobTinder/login.html', {})


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/#')
        else:
            messages.error(request, 'Usuario  e senha inválidos. :(')
    return redirect('/')
