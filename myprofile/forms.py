from django import forms
from django.forms import ModelForm


class ContactForm(forms.Form):

    from_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your message...'}), required=True)
