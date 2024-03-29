from django import forms
from .models import sellDog
from .models import sellCat
from .models import doctor
from .models import feedbackone

class sellDogForm(forms.ModelForm):
    class Meta:
        model = sellDog
        fields = ['username', 'breed','age', 'img', 'price', 'phone','address']

class sellCatForm(forms.ModelForm):
    class Meta:
        model = sellCat
        fields = ['username', 'breed','age', 'img', 'price', 'phone','address']

class doctorForm(forms.ModelForm):
    class Meta:
        model = doctor
        fields = ['username', 'pet', 'email', 'address', 'phone', 'reason']

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedbackone
        fields = ['name', 'phone', 'email', 'subject', 'message']

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail", 'style': 'margin-bottom: 10px;'})
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Enter reason", 'style': 'margin-bottom: 10px;'})
    )