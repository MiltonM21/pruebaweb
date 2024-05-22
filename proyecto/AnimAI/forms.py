from django import forms

class userForm(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}))
    contraseña = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))


class loginForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Apellido'}))
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}))
    contraseña = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    telefono = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}))

class testUser(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()