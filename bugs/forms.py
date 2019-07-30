from django import forms
from .models import Bugs


class BugsPostForm(forms.ModelForm):

    class Meta:
        model = Bugs
        fields = ('title', 'description', 'image', 'published_date')