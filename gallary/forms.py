from django import forms
from .models import *
from multiupload.fields import MultiFileField

class GallaryImageForm(forms.ModelForm):
    pic = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }), label = "")
    class Meta:
        model = GallaryImage
        fields = ['pic']