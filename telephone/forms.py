from django import forms
from . import models

class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Добавить комментарий'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['stars', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Добавить комментарий'}),
        }
