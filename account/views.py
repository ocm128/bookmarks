from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.

def user_login(request):

    # When the user submits the form via POST
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # Authenticates the user against the db. Returns a object user
            user = authenticate(username=cd['username'],
                                             password=cd['password'])

            if user is not None:
                if user.is_active:

                    # Sets the user in the current session
                    login(request, user)
                    return HttpResponse('Authenticated successfully')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        # When user_login() is called with a GET request
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
