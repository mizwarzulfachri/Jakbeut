from django.forms import ModelForm
from django import forms
from App.models import User, Ceramah

class FormCeramah(ModelForm):
    Judul = forms.CharField(required=False)
    Deskripsi = forms.CharField(required=False)
    Tanggal = forms.DateField(required=False)
    Waktu = forms.TimeField(required=False)
    Images = forms.ImageField(required=False)
    Link =  forms.URLField(required=False)

    class Meta:
        model = Ceramah
        fields = ['Judul', 'Deskripsi', 'Tanggal', 'Waktu', 'Images', 'Link']