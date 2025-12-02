from django.shortcuts import render


# Create your views here.
a = "Senai"

def home(request):
    return render(request, "page/home.html", context={'nome': a,})

def receita(request):
    return render(request, 'page/receita-view.html', context={'nome': a,})
