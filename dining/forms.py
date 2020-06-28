from django import forms
from .models import Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
