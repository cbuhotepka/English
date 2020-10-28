from django import forms
from .models import UserVocabulary

class UserVocabularyForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title..', 'id': 'id_title'}),
    )
     
    class Meta:
        model = UserVocabulary
        fields = ['title',]