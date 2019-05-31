from django import forms
from .models import contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = contract
        fields = '__all__'

