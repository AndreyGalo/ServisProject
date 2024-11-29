from .models import AutomobilioModelis, Paslauga, Uzsakymas
from django.shortcuts import render

def index(request):
    auto_modeliai = AutomobilioModelis.objects.all().count()
    paslaugos = Paslauga.objects.all().count()
    atlikti_uzsakymai = Uzsakymas.objects.all().filter(status__exact="p").count()
    context = {
        "atlikti_uzsakymai" : atlikti_uzsakymai,
        "paslaugos" : paslaugos,
        "auto_modeliai": auto_modeliai
    }
    return  render(request,"index.html",context=context)
