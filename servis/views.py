from django.core.paginator import Paginator
from django.views import generic
from .models import AutomobilioModelis, Paslauga, Uzsakymas, Automobilis
from django.shortcuts import render , get_object_or_404
from django.db.models import Q

def index(request):
    auto_modeliai = AutomobilioModelis.objects.all().count()
    paslaugos = Paslauga.objects.all().count()
    atlikti_uzsakymai = Uzsakymas.objects.all().filter(status__exact="p").count()
    num_visits = request.session.get("num_visits",1)
    request.session["num_visits"] = num_visits + 1
    context = {
        "atlikti_uzsakymai" : atlikti_uzsakymai,
        "paslaugos" : paslaugos,
        "auto_modeliai": auto_modeliai,
        "num_visits": num_visits,
    }
    return  render(request,"index.html",context=context)

def automobiliai(request):
    paginator = Paginator(Automobilis.objects.all(),3)
    page_number = request.GET.get("page")
    automobiliai = paginator.get_page(page_number)
    # automobiliai = Automobilis.objects.all()
    context = {"automobiliai": automobiliai}
    return render(request,"automobiliai.html",context=context)

def automobilis(request,automobilis_id):
    vienas_automobilis = get_object_or_404(Automobilis,pk=automobilis_id)
    return render(request,"automobilis.html",{"automobilis": vienas_automobilis})

class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 4
    template_name = "uzsakymai_list.html"

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = "uzsakymas_detail.html"

def apiemus(request):
    return render(request,"apiemus.html")

def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(Q(Klientas__icontains=query) | Q(Valstybinis_NR__icontains=query) | Q(VIN_kodas__icontains=query) | Q(AutomobilioModelis__Marke__icontains=query)| Q(AutomobilioModelis__Modelis__icontains=query))
    return render(request, 'search.html', {'automobiliai': search_results, 'query': query})