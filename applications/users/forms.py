from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    password1= forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2= forms.CharField(
        label='Repetir contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""
        model = User
        fields = (
            'username',
            'email',
            'full_name',
            'apellidos',
            'genero',
            'ocupation',
            'fecha_nacimiento',

        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son las mismas')
        if len(self.cleaned_data['password1']) < 5:
            self.add_error('password1','las contraseña es muy corta')


class LoginForm(forms.Form):
    username= forms.CharField(
        label='username',
        required= True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': '{ margin: 10px }',
            }
        )
    )
    password= forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data= super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')

        return self.cleaned_data 

class UpdatePasswordForm(forms.Form):
    password1= forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual'
            }
        )
    )
    password2= forms.CharField(
        label='Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )

class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)

    
    def __init__(self,pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    #validaciones siempre con clean
    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            #verificamos si el codigo y el id de usuario son validos

            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('Los datos del usuario no son correctos')
        else:
            raise forms.ValidationError('codigo incorrecto')

