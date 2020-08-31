from django import forms
from .models import Customer
from myAuth.models import User


class CustomerUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta():
        model = User
        fields = ('full_name', 'email', 'phone')
class CustomerForm(forms.ModelForm):
    class Meta():
        model=Customer
        fields =('Address','Phone2')



