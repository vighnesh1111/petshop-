from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail", 'style': 'margin-bottom: 25px;'})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject", 'style': 'margin-bottom: 25px;'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message", 'style': 'margin-bottom: 10px;'})
    )