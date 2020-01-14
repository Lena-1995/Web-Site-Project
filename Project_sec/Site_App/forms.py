from django import forms
from .models import *


class SingInForm(forms.ModelForm):
    class Meta:
        model = SingIn
        exclude = [""]
