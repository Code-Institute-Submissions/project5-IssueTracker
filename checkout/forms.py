from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2035)]
    
    credit_card_number = forms.CharField(label = "credit card number", required=False)
    cvv = forms.CharField(label = "Security number (CVV)", required=False)
    expiry_month = forms.ChoiceField(label = "Expiry Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label = "Expiry year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('full_name',)