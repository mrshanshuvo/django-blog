from django import forms
from .models import Author
from django.core import validators


def start_s(value):
    if value[0] not in ["s", "S"]:
        raise forms.ValidationError("Name should start with letter s/S")


class AuthorsForm(forms.ModelForm):
    name = forms.CharField(
        validators=[validators.MaxLengthValidator(10), start_s],
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Your Name",
    )
    email = forms.CharField(
        validators=[validators.MaxLengthValidator(10), start_s],
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Your Email",
    )

    class Meta:
        model = Author
        fields = "__all__"
        labels = {
            "contact_no": "Contact Number",
            "bio": "Your Details",
        }
        widgets = {
            "contact_no": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control"}),
        }
        help_texts = {"email": "We only accept gmail"}
        error_messages = {"name": {"required": "Name field is required"}}
