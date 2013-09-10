from django import forms

class EditProfileForm(forms.Form):
    bio = forms.CharField(label='About me', widget=forms.Textarea)
    picture = forms.ImageField(label='Profile picture', required=False)

class NewPostForm(forms.Form):
    message = forms.CharField(max_length=140, widget=forms.Textarea)
