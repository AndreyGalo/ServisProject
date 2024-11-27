from django.db import models


class Automobilio_modelis(models.Model):
    Marke = models.CharField("Markės pavadinimas", max_length=30, null=False)
    Modelis = models.CharField("Modelio pavadinimas", max_length=30, null=False)

    def __str__(self):
        return f"Marke: {self.Marke}. Modelis: {self.Modelis}"


class Automobilis(models.Model):
    Valstybinis_NR = models.CharField("Mašinos valstybinis numeris", max_length=10, null=False)
    VIN_kodas = models.CharField("Mašinos VIN numeris/kodas", max_length=25, null=False)
    Klientas = models.CharField("Kliento Vardas Pavardė", max_length=50, null=False)
    Automobilio_modelis = models.ForeignKey("Automobilio_modelis", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"NR: {self.Valstybinis_NR}. VIN: {self.VIN_kodas}. Klientas: {self.Klientas}. {self.Automobilio_modelis}"


class Uzsakymas(models.Model):
    Data = models.DateField("Data", null=False)
    Automobilis = models.ForeignKey("Automobilis", on_delete=models.CASCADE,null=False)

    def __str__(self):
        return f"Uzsakymo data: {self.Data}  {self.Automobilis}"


class Paslauga(models.Model):
    Pavadinimas = models.TextField("Aprašymas", max_length=500, help_text='Trumpas paslaugos aprašymas')
    Kaina = models.IntegerField("Kaina",null=False,help_text="Ivedama kaina")

    def __str__(self):
        return f"Paslauga: {self.Pavadinimas}. Kaina: {self.Kaina}"


class Uzsakymo_eilute(models.Model):
    Paslauga = models.ForeignKey("Paslauga", on_delete=models.CASCADE, null=False)
    Uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE, null=False)
    Kiekis = models.CharField("Paslaugu kiekis", max_length=10, null=False)

    def __str__(self):
        return f"{self.Paslauga} {self.Uzsakymas}. Uzsakymu kiekis: {self.Kiekis}"
