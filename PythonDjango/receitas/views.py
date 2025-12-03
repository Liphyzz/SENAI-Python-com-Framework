from django.shortcuts import render
from receitas.fabrica.receitasFake import gen_fake_receita


# Create your views here.
a = "Senai"

def home(request):
    return render(request, "page/home.html", context={'nome': a,'receitas': [gen_fake_receita() for _ in range(10)],})

def receita(request):
    return render(request, 'page/receita-view.html', context={'nome': a, 'receita': gen_fake_receita()})
