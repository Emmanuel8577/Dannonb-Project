from django import forms

from website.models import Donation


from .models import PartnershipSubmission


from django import forms
from .models import PartnershipSubmission


# forms.py
from django import forms
from .models import PartnershipSubmission


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = PartnershipSubmission
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "organisation",
            "partnership_category",
            "message",
        ]
        widgets = {
            "message": forms.Textarea(
                attrs={"rows": 4, "placeholder": "How do you want to support us?"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].initial = ""


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Your Email"}
        )
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Phone"}
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Your Message", "rows": 5}
        )
    )


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "organization",
            "partnership_category",
            "message",
        ]
