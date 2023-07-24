from django import forms
from .models import add_user

class Model_Add_U(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Model_Add_U, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['document'].label = ""
        self.fields['email'].label = ""
        self.fields['age'].label = "Edad"

    class Meta:
        model=add_user
        fields=['name','last_name','document','email','age']
        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder': 'Nombre'}),
            'last_name'    : forms.TextInput(attrs = {'placeholder': 'Apellido'}),
            'document'    : forms.TextInput(attrs = {'placeholder': 'N° identificación'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'Email'}),

        }
