from django.db import models


class AutomobilioModelis(models.Model):
    Marke = models.CharField("Markės pavadinimas", max_length=30, null=False)
    Modelis = models.CharField("Modelio pavadinimas", max_length=30, null=False)

    def __str__(self):
        return f"{self.Marke} {self.Modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobiliu modeliai"


class Automobilis(models.Model):
    Valstybinis_NR = models.CharField("Mašinos valstybinis numeris", max_length=10, null=False)
    VIN_kodas = models.CharField("Mašinos VIN numeris/kodas", max_length=25, null=False)
    Klientas = models.CharField("Kliento Vardas Pavardė", max_length=50, null=False)
    AutomobilioModelis = models.ForeignKey("AutomobilioModelis", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"Automobilio NR: {self.Valstybinis_NR}. Klientas: {self.Klientas}"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"


class Uzsakymas(models.Model):
    Data = models.DateField("Data", null=False)
    Automobilis = models.ForeignKey("Automobilis", on_delete=models.CASCADE, null=False)

    UZS_STATUS = (
        ("v", "Vykdoma"),
        ("l", "Laukiama"),
        ("p", "Paruošta"),
        ("n", "Nukelta"),
    )
    status = models.CharField(
        max_length=1,
        choices=UZS_STATUS,
        blank=True,
        default="l",
        help_text="Statusas"
    )

    def __str__(self):
        return f"Uzsakymo data: {self.Data}  {self.Automobilis} {self.status}"

    class Meta:
        ordering = ["Data"]
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"


class Paslauga(models.Model):
    Pavadinimas = models.TextField("Aprašymas", max_length=200, help_text='Trumpas paslaugos aprašymas')
    Kaina = models.IntegerField("Kaina", null=False, help_text="Ivedama kaina")

    def __str__(self):
        return f"{self.Pavadinimas}. Kaina: {self.Kaina}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


class UzsakymoEilute(models.Model):
    Paslauga = models.ForeignKey("Paslauga", on_delete=models.CASCADE, null=False)
    Uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE, null=False)
    Kiekis = models.IntegerField("Paslaugu kiekis", null=False)

    def __str__(self):
        return f"{self.Paslauga} {self.Uzsakymas}. Uzsakymu kiekis: {self.Kiekis}"

    class Meta:
        verbose_name = "Užsakymų suvestinė"
        verbose_name_plural = "Užsakymų suvestinė"
