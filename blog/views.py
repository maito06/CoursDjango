from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime


def home(request):
    return

def date_actuelle(request):
    couleurs = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
    return render(request, 'blog/date.html', {'date': datetime.now(), 'couleurs': couleurs})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    return render(request, 'blog/addition.html', locals())
    

