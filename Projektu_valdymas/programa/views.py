from django.shortcuts import render
from .models import Klientas, Darbuotojas, Darbas , Saskaita , Projektas


def index(request):
    num_klientai = Klientas.objects.all().count()
    num_darbuotojai = Darbuotojas.objects.all().count()
    num_darbai = Darbas.objects.count()
    num_saskaitos = Saskaita.objects.count()
    num_projektai = Projektas.objects.count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_klientai': num_klientai,
        'num_darbuotojai': num_darbuotojai,
        'num_darbai': num_darbai,
        'num_saskaitos': num_saskaitos,
        'num_projektai': num_projektai,

    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)
