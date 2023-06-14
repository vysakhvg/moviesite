from html.entities import html5
from django import forms
from movieapp.models import movie


class movieform(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['name', 'description', 'year', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
