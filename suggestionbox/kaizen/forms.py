from django import forms
from django.db import models
from django.forms import ModelForm
from kaizen.models import Idea

class NewIdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('category', 'title', 'body',)

        
