from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as logout_user, login as login_user


def register(request):
    """Register form."""
    return render(request, 'users/profile.html', {})


def login(request):
    """Main login view. Handling login form and redirects after login."""
    if request.user.is_authenticated():
        return redirect("/users/profile/")

    error_message = ""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login_user(request, user)
            if "next" in request.GET:
                return redirect(request.GET["next"])
            else:
                return redirect("/users/profile/")
        else:
            error_message = "wrong username or password"

    return render(request, 'users/login.html', {"error_message":error_message})


@login_required
def profile(request):
    """Users profile view."""
    return render(request, 'users/profile.html', {})


@login_required
def logout(request):
    """Logouts user"""
    logout_user(request)
    return redirect("/users/login")

