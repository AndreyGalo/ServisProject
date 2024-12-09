from django.contrib.auth.models import User

from .models import UzsakymasAtsiliepimas, Profilis
from django import forms

class UzsakymasAtsiliepimasForm(forms.ModelForm):
    class Meta:
        model = UzsakymasAtsiliepimas
        fields = ("content","uzsakymas","atsiliepimas",)
        widgets = {"uzsakymas": forms.HiddenInput(),"atsiliepimas": forms.HiddenInput()}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']