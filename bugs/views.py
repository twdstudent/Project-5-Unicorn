from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bugs
from .forms import BugsPostForm

def get_bugs(request):
    """
    This will create view that will return a list
    of Bugs that were posted prior to 'now'
    and render them to the 'bugs.html' template
    """
    bug = Bugs.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "bugs.html", {'bug': bug})

def bugs_detail(request, pk):
    """
    Create a view that returns a single
    Bug object based on the post ID (pk) and
    render it to the 'bug-detail.html' template.
    Or return a 404 error if the bug isn't found
    """
    bug = get_object_or_404(Bugs, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bug-detail.html", {'bug': bug})
    
def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to post a new
    or edit a existing bug depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bugs, pk=pk) if pk else None
    if request.method == "POST":
        form = BugsPostForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            post = form.save()
            return redirect(bugs_detail, post.pk)
    else:
        form = BugsPostForm(instance=post)
    return render(request, 'bug-post-form.html', {'form': form})    