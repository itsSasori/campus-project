from django import forms
from .models import *
#Create your forms here:
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
