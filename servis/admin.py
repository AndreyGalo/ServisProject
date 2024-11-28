from django.contrib import admin
from .models import Automobilio_modelis, Automobilis, Uzsakymas, Paslauga, Uzsakymo_eilute


class UzsakymoEiluteInline(admin.TabularInline):
    model = Uzsakymo_eilute
    extra = 1
    can_delete = False


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("Automobilis", "Data")
    inlines = [UzsakymoEiluteInline]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("Klientas", "Automobilio_modelis", "Valstybinis_NR", "VIN_kodas")
    list_filter = ("Klientas","Automobilio_modelis")
    search_fields = ("Valstybinis_NR","VIN_kodas")
    search_help_text = "Paieška pagal Automobilio valstybini Numerį arba VIN Kodą"


class PaslaugosAdmin(admin.ModelAdmin):
    list_display = ("Pavadinimas", "Kaina")


admin.site.register(Automobilio_modelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga,PaslaugosAdmin)
admin.site.register(Uzsakymo_eilute)
