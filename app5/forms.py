from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Name need to start with - a')

class NameForm(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField(label="Email address:")
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea,
                            validators=[validators.MaxLengthValidator(5)])
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vemail = cleaned_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Make sure email match')
        return cleaned_data
