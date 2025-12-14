from django import forms
class AuthorsForm(forms.Form):
  name = forms.CharField()
  