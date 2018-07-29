from django import forms
from django.core import validators


class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
