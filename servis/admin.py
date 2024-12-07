from django.contrib import admin
from .models import AutomobilioModelis, Automobilis, Uzsakymas, Paslauga, UzsakymoEilute


class UzsakymoEiluteInLine(admin.TabularInline):
    model = UzsakymoEilute
    extra = 1
    can_delete = False


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("automobilis","status","data","vartotojas","due_back")
    list_editable = ("status",)
    inlines = [UzsakymoEiluteInLine]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ("klientas", "automobiliomodelis", "valstybinis_nr", "vin_kodas")
    list_filter = ("klientas","automobiliomodelis")
    search_fields = ("valstybinis_nr","vin_kodas")
    search_help_text = "Paieška pagal Automobilio valstybini Numerį arba VIN Kodą"


class PaslaugosAdmin(admin.ModelAdmin):
    list_display = ("pavadinimas", "kaina")


admin.site.register(AutomobilioModelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga,PaslaugosAdmin)
admin.site.register(UzsakymoEilute)
