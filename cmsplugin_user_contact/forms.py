# -*- coding: utf-8 -*-
__author__ = 'Kirill S. Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from django import forms
from models import UserContact


class UserContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea())

    def clean(self):
        self.cleaned_data['subject'] = 'Geometrical community'
        return self.cleaned_data


class UserContactAdminForm(forms.ModelForm):

    class Meta:
        model = UserContact