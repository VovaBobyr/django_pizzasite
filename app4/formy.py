from django import forms
from app4.models import Order
from app4.models import Pizza

class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')
