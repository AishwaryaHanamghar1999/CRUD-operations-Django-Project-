from django import forms
from .models import emp_info

class emp_form(forms.ModelForm):
    
    class Meta:
        model = emp_info
        fields = '__all__'
