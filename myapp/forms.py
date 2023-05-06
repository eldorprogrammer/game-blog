from django import forms
from .models import Profil,Turnir,Contact


class Profil1(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'

class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['image']



class TurnirQoshish(forms.ModelForm):
    class Meta:
        model = Turnir
        fields = '__all__'

class TurnirUpdateForm(forms.ModelForm):
    class Meta:
        model = Turnir
        fields = '__all__'


class ContactUpdate(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email','massage','subject']


