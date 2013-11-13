from django.forms import ModelForm
from binpaste.models import Bin

class NewBinForm(ModelForm):
    
    class Meta:
        model = Bin
        fields = ['title', 'text', 'language']
    
