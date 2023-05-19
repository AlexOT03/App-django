from django import forms
from .models import Places,Orders,Message

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        exclude = {"places"}

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"