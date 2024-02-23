from django import forms


class PlantTreeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    scientific_name = forms.CharField(max_length=100, required=True)
    account = forms.IntegerField(required=True)
    longitude = forms.DecimalField(required=True)
    latitude = forms.DecimalField(required=True)
