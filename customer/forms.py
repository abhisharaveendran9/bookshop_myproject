from django import forms

class CartForm(forms.Form):
    qty=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))


class OrderForm(forms.Form):
    delivery_address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))