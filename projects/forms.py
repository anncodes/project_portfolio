from django import forms


class ContactForm(forms.Form):
    sender_name = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your name"
        })
    )
    from_email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your email"
        }),
        required=True
        )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Your message"
        }),        
        required=True
        )