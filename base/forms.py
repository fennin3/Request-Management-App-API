from django import  forms
from .models import  Request



class RequestForm(forms.ModelForm):
    # request_type = forms.CharField(max_length=100, , label="Request Type", required=True)
    class Meta:
        model=Request
        fields="__all__"