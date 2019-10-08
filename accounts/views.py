from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bugs
from bugs.views import get_bugs, upvote_bug, bugs_detail, create_or_edit_bug 
from feature.models import Feature
from feature.views import get_feature, feature_detail, create_or_edit_feature 

#accounts views

def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

def user_profile(request):
    """The user's profile page"""
    bug = Bugs.objects.filter(owner=request.user)
    feature = Feature.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'bug':bug, 'feature':feature})
    
def get_user_bugs(request):
    """
    This will create view that will return a list
    of Bugs that were posted prior to 'now'
    and render them to the 'bugs.html' template
    """
    bug = Bugs.objects.filter(published_date__lte=timezone.now()
        ).order_by('published_date')
    return render(request, "profile.html", {'bug': bug})
    
