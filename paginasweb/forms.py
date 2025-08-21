
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Especialidade

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade  
        fields = ['nome', 'descricao']  


class UsuarioCadastroForm(UserCreationForm):


    email = forms.EmailField(required=True, help_text="Informe um email válido.")


    
    class Meta:
        model = User
       
        fields = ['username', 'email', 'password1', 'password2']


    
    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email
