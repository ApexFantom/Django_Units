from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from .models import Unitsdb
from django.forms import ModelForm, TextInput, Textarea,  ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.password_validation
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

# If you don't like <iframe>, then use inplace widget
# Or if you're using django-crispy-forms, please use this.
class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())
class UnitsForm(ModelForm):
    class Meta:
        model = Unitsdb
        fields = ['name', 'fr', 'type', 'short_des', 'des', 'img', 'img_bck']

        widgets = {
            'name': TextInput(attrs={
                'class':"form__input",
                    'id':"name",
                'placeholder':"Unit name",
                'value': "",
            }),
            'fr': TextInput(attrs={
                'class': "form__input",
                'id': "fr",
                'placeholder': "Unit fraction",
                'value': "P",
                'style': "display:none;",
            }),
            'type': TextInput(attrs={
                'class': "form__input",
                'id': "type",
                'placeholder': "Unit type",
                'value': "",
            }),
            'short_des': Textarea(attrs={
                'class': "form__input",
                'id': "des",
                'placeholder': "Unit description",
                'value': "",
                'style': "resize:none",
            }),
            'des': SummernoteWidget(),

            'img_bck':  ClearableFileInput(attrs={
                'class': "file-input",
                'id': "img_bck",
                'value': "",
            }),
            'img':  ClearableFileInput(attrs={
                'class': "file-input",
                'id': "img",
                'value': "",
            }),
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login:', widget=forms.TextInput(attrs={'class': 'blank-input'}))
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class': 'blank-input'}))
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput(attrs={'class': 'blank-input'}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')
    # widgets = {
    #         'username': forms.TextInput(attrs={'class': 'blank-input'}),
    #         'password1': forms.PasswordInput(attrs={'class': 'blank-input'}, ),
    #         'password2': forms.PasswordInput(attrs={'class': 'blank-input'}, ),
    #     }
    #

    # def __init__(self, *args, **kwargs):
    #     super(UserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].help_text = ''
    #     self.fields['password'].help_text = ''


    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')
    #



 # help_text=password_validation.password_validators_help_text_html()),
