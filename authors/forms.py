from django import forms
from .models import Author


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email", "contact_no", "bio"]

        # custom labels (optional)
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "contact_no": "Contact Number",
            "bio": "Your Details",
        }

        # custom css (optional)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "contact_no": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control"}),
        }

        # customer help texts (optional)
        help_texts = {"email": "We only accept gmail"}

        # customer error messages (optional)
        error_messages = {"name": {"required": "Name field is required"}}
