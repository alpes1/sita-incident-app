from django import forms 
from django.forms import ModelForm,HiddenInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'password1',
            'password2',  
              ]
        
class SiteForm(ModelForm):
    class Meta:
        model = Site 
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set 'required' to False for specific fields
        self.fields['closed_at'].required = False
        self.fields['solution'].required = False
        self.fields['probleme'].required = False
        
        
        