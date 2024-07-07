from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Account
from django import forms


User = get_user_model()

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['country', 'city', 'address', 'ZIP', 'phone', 'email']

