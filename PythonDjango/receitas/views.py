from django.shortcuts import render
from django.http import HttpResponse

a = 10
    
def home(request):
    return render(request, "home.html",
            context=
                {
                    'nome' : a,
                })

def sobre(request):
    return HttpResponse("Sobre nóis")

def receitas(request):
    return HttpResponse("Receitas")
