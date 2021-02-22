from django import forms

from .models import Person

class PersonModelForm(froms.ModelForm):
    class Meta:
        model  = Person
        fields = '__all__'
