from django import forms
from .models import registration

class registrationForm(forms.ModelForm):
    class Meta:
        model = registration
        fields ='__all__'

 