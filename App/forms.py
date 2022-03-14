from django import forms
from App.models import Information


class infoForm(forms.ModelForm):

    class Meta:
        model=Information
        fields=['name','email','profile_pic']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
            
        }