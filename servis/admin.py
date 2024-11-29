from django.contrib import admin
from .models import AutomobilioModelis, Automobilis, Uzsakymas, Paslauga, UzsakymoEilute


class UzsakymoEiluteInLine(admin.TabularInline):
    model = UzsakymoEilute
    extra = 1
    can_delete = False


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("Automobilis", "Data")
    inlines = [UzsakymoEiluteInLine]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("Klientas", "AutomobilioModelis", "Valstybinis_NR", "VIN_kodas")
    list_filter = ("Klientas","AutomobilioModelis")
    search_fields = ("Valstybinis_NR","VIN_kodas")
    search_help_text = "Paieška pagal Automobilio valstybini Numerį arba VIN Kodą"


class PaslaugosAdmin(admin.ModelAdmin):
    list_display = ("Pavadinimas", "Kaina")


admin.site.register(AutomobilioModelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga,PaslaugosAdmin)
admin.site.register(UzsakymoEilute)
