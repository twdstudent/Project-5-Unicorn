from django import forms
from .models import Feature


class FeaturesPostForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('title', 'description', 'published_date')