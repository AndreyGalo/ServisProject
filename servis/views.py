from django.views import generic
from django.http import HttpResponse
from .models import AutomobilioModelis, Paslauga, Uzsakymas, Automobilis , UzsakymoEilute
from django.shortcuts import render , get_object_or_404

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

def automobiliai(request):
    automobiliai = Automobilis.objects.all()
    context = {"automobiliai":automobiliai}
    return render(request,"automobiliai.html",context=context)

def automobilis(request,automobilis_id):
    vienas_automobilis = get_object_or_404(Automobilis,pk=automobilis_id)
    return render(request,"automobilis.html",{"automobilis": vienas_automobilis})

class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    template_name = "uzsakymai_list.html"

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = "uzsakymas_detail.html"
