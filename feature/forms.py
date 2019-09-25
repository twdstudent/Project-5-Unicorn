from django import forms
from .models import Feature


class FeaturesPostForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('title', 'content', 'published_date', 'status', 'owner')