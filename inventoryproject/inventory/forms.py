from django import forms

class EditItemQty(forms.Form):
    quantity = forms.IntegerField()
