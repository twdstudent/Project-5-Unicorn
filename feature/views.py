from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Feature
from .forms import FeaturesPostForm

# Create your views here.
    
def get_feature(request):
    """
    This will create view that will return a list
    of Features that were posted prior to 'now'
    and render them to the 'feature.html' template
    """
    feature = Feature.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "feature.html", {'feature': feature})
    
def feature_detail(request, pk):
    """
    Create a view that returns a single
    Feature object based on the post ID (pk) and
    render it to the 'feature-detail.html' template.
    Or return a 404 error if the feature isn't found
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    return render(request, "feature-detail.html", {'feature': feature})
    
def create_or_edit_feature(request, pk=None):
    """
    Create a view that allows us to post a new
    or edit a existing bug depending if the Post ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeaturesPostForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            post = form.save()
            return redirect(feature_detail, post.pk)
    else:
        form = FeaturesPostForm(instance=post)
    return render(request, 'feature-post-form.html', {'form': form})     