from django import forms
from .models import personal, company, documentation


class personalform(forms.ModelForm):
    class Meta:
        model = personal
        fields = '__all__'


class companyform(forms.ModelForm):
    class Meta:
        model = company
        fields = '__all__'


class documentform(forms.ModelForm):
    class Meta:
        model = documentation
        fields = '__all__'
