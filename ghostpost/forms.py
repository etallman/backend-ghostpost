from django import forms
from ghostpost.models import AnonUser, Boast, Roast


class BoastForm(forms.Form):
    boast = forms.CharField(label="boast", max_length=280,widget=forms.Textarea)
    # boast_data = forms.ModelChoiceField(queryset=Boast.objects.all())

    
class RoastForm(forms.Form):
    roast = forms.CharField (label="roast", max_length=280,widget=forms.Textarea)
    # roast_data = forms.ModelChoiceField(queryset=Roast.objects.all())