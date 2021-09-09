from django import forms

from .models import *

class CreateProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = "__all__"

class AreaForm(forms.ModelForm):
    class Meta:
        model = Service_area
        fields = "__all__"