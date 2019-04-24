from django.shortcuts import render
from .models import Feature

# Create your views here.
def all_feature(request):
    feature = Feature.objects.all()
    return render(request, "feature.html", {"feature": Feature})