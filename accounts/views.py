from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bugs
from feature.models import Feature


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
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
    
@login_required
def bugs_detail(request, pk):
    """A view that displays the profile page of a logged in user"""
    bug = Bugs.objects.filter(author=request.user)
    feature = Feature.objects.filter(author=request.user)
    return render(request, 'profile.html', {'bugs':bug, 'feature':feature})

#def bugs_detail(request, pk):
#    """
#    Create a view that returns a single
#    Bug object based on the post ID (pk) and
#    render it to the 'bug-detail.html' template.
#    Or return a 404 error if the bug isn't found
#    """
#    bug = get_object_or_404(Bugs, pk=pk)
#    bug.views += 1
#    bug.save()
#    return render(request, "profile.html", {'bug': bug})    