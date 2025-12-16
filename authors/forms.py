from django import forms
from .models import Author


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email", "contact_no", "bio"]
