from django import forms
from tinymce.widgets import TinyMCE

class EditItemQty(forms.Form):
    quantity = forms.IntegerField()

class CategoryForm(forms.Form):
    name = forms.CharField(max_length = 100)
    description = forms.CharField(widget = TinyMCE(attrs = {'cols': 80, 'rows': 5}), required=False)
