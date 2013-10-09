from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from inventory.models import Category

class EditItemQty(forms.Form):
    quantity = forms.IntegerField()

class CategoryForm(ModelForm):
    class Meta:
        model = Category

# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length = 100)
#     description = forms.CharField(widget = TinyMCE(attrs = {'cols': 80, 'rows': 5}), required=False)
#     image = forms.ImageField()
