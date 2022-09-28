from django import forms

class PetRegistrationForm(forms.Form):
    name = forms.CharField()
    birth = forms.DateField()
    color = forms.CharField()