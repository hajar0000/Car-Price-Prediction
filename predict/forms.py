# predict/forms.py
from django import forms

class PredictionForm(forms.Form):
    Present_Price = forms.FloatField(
        label="Prix actuel ", 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez le prix actuel"})
    )
    Age = forms.IntegerField(
        label="Âge de la voiture (en années)", 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez l'âge"})
    )
    Kms_Driven = forms.IntegerField(
        label="Kilomètres parcourus", 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez les kilomètres parcourus"})
    )
    Seller_Type = forms.ChoiceField(
        choices=[(2, "Concessionnaire"), (3, "Particulier")], 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    Fuel_Type = forms.ChoiceField(
        choices=[(2, "Diesel"), (3, "Essence"), (4, "CNG")], 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    Transmission = forms.ChoiceField(
        choices=[(2, "Automatique"), (3, "Manuelle")], 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    Owner = forms.IntegerField(
        label="Nombre de propriétaires précédents", 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Entrez le nombre de propriétaires"})
    )
