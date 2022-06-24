
from pyexpat import model
from .models import Register
from django import forms

class RegisterForm(forms.Form):
    class data:
        model=Register
        field=[
            'Name','Seat','Date'
        ]
