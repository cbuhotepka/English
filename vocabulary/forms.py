from django import forms
from .models import UserWordset

class UserWordsetForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title..', 'id': 'id_title'}),
    )
     
    class Meta:
        model = UserWordset
        fields = ['title',]