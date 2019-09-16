from django import forms
from .models import Bugs


class BugsPostForm(forms.ModelForm):

    class Meta:
        model = Bugs
        fields = ('title', 'content', 'image', 'published_date', 'owner')