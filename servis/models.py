import datetime
from datetime import date
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


class AutomobilioModelis(models.Model):
    marke = models.CharField("Markės pavadinimas", max_length=30, null=False)
    modelis = models.CharField("Modelio pavadinimas", max_length=30, null=False)

    def __str__(self):
        return f"{self.marke} {self.modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobiliu modeliai"


class Automobilis(models.Model):
    valstybinis_nr = models.CharField("Mašinos valstybinis numeris", max_length=10, null=False)
    vin_kodas = models.CharField("Mašinos VIN numeris/kodas", max_length=25, null=False)
    klientas = models.CharField("Kliento Vardas Pavardė", max_length=50, null=False)
    automobiliomodelis = models.ForeignKey("AutomobilioModelis", on_delete=models.CASCADE, null=False)
    aprasymas = HTMLField(null=True, blank=True)
    cover = models.ImageField('Nuotrauka', upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"Automobilio NR: {self.valstybinis_nr}. Klientas: {self.klientas}"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"


class Uzsakymas(models.Model):
    data = models.DateField("Data", null=False,default=datetime.date.today)
    automobilis = models.ForeignKey("Automobilis", on_delete=models.CASCADE, null=False)
    vartotojas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField("Paruosimo data", null=True, blank=True)

    @property
    def pradelstas_uzsakymas(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

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
        return f"Uzsakymo data: {self.data}  {self.automobilis} {self.status}"

    class Meta:
        ordering = ["data"]
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"


class Paslauga(models.Model):
    pavadinimas = models.TextField("Aprašymas", max_length=200, help_text='Trumpas paslaugos aprašymas')
    kaina = models.IntegerField("Kaina", null=False, help_text="Ivedama kaina")

    def __str__(self):
        return f"{self.pavadinimas}. Kaina: {self.kaina}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


class UzsakymoEilute(models.Model):
    paslauga = models.ForeignKey("Paslauga", on_delete=models.CASCADE, null=False)
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE, null=False)
    kiekis = models.IntegerField("Paslaugu kiekis", null=False)

    def __str__(self):
        return f"{self.paslauga} {self.uzsakymas}. Uzsakymu kiekis: {self.kiekis}"

    class Meta:
        verbose_name = "Užsakymų suvestinė"
        verbose_name_plural = "Užsakymų suvestinė"


class UzsakymasAtsiliepimas(models.Model):
    uzsakymas = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True, blank=True)
    atsiliepimas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas', max_length=2000)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']

class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)

    class Meta:
        verbose_name = "Profilis"
        verbose_name_plural = "Profiliai"
