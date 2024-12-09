from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from .forms import UzsakymasAtsiliepimasForm, UserUpdateForm, ProfilisUpdateForm
from .models import AutomobilioModelis, Paslauga, Uzsakymas, Automobilis
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q


def index(request):
    auto_modeliai = AutomobilioModelis.objects.all().count()
    paslaugos = Paslauga.objects.all().count()
    atlikti_uzsakymai = Uzsakymas.objects.all().filter(status__exact="p").count()
    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1
    context = {
        "atlikti_uzsakymai": atlikti_uzsakymai,
        "paslaugos": paslaugos,
        "auto_modeliai": auto_modeliai,
        "num_visits": num_visits,
    }
    return render(request, "index.html", context=context)


def automobiliai(request):
    paginator = Paginator(Automobilis.objects.all().order_by("id"), 6)
    page_number = request.GET.get("page")
    automobiliai = paginator.get_page(page_number)
    # automobiliai = Automobilis.objects.all()
    context = {"automobiliai": automobiliai}
    return render(request, "automobiliai.html", context=context)


def automobilis(request, automobilis_id):
    vienas_automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, "automobilis.html", {"automobilis": vienas_automobilis})


class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 4
    template_name = "uzsakymai_list.html"


class UzsakymasDetailView(FormMixin, generic.DetailView):
    model = Uzsakymas
    template_name = "uzsakymas_detail.html"
    form_class = UzsakymasAtsiliepimasForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('uzsakymas', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.uzsakymas = self.object
        form.instance.atsiliepimas = self.request.user
        form.save()
        return super(UzsakymasDetailView, self).form_valid(form)


def apiemus(request):
    return render(request, "apiemus.html")


def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(
        Q(klientas__icontains=query) | Q(valstybinis_nr__icontains=query) | Q(vin_kodas__icontains=query) | Q(
            automobiliomodelis__marke__icontains=query) | Q(automobiliomodelis__modelis__icontains=query))
    return render(request, 'search.html', {'automobiliai': search_results, 'query': query})


class UzsStatusasPagalVartotoja(LoginRequiredMixin, generic.ListView):
    model = Uzsakymas
    template_name = 'varototojo_uzsakymai.html'
    paginate_by = 3

    def get_queryset(self):
        return Uzsakymas.objects.filter(vartotojas=self.request.user).order_by('data')


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html',context)
