from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse

# Importing the packages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'basic_app/index.html')

# Here is special method


@login_required
def special(request):
    return HttpResponse("You are logged in successful")

# Here is logout method


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # DB

        if user_form.is_valid() and profile_form.is_valid():

            # Save USER TO DB
            user = user_form.save()

            # This logic is setting the password to DB AS hashed
            user.set_password(user.password)

            user.save()

            # This is checking if this info exist in the DB BY SETTING IT TO FALSE
            profile = profile_form.save(commit=False)

            profile.user = user

            # Checking if there is profile pict from this new user
            if 'profile_pic' in request.FILES:
                print('Found It!')

                profile.profile_pic = request.FILES['profile_pic']

                # Here is saving the profile pic to a DIR callled profile_pic on the project DIR and keeping ref in the DB tuple
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'basic_app/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
# #Loging here
# def login(request):


def userLogin(request):
    # If statement for checking the POST data
    if request.method == 'POST':
        # This variables grab the data from the HTML form
        # which contained username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Here is Django auth method
        user = authenticate(username=username, password=password)

        # Checking if the user is active
        if user:
            if user.is_active:
                # Log the user in
                login(request, user)
                # This send the user to a page when login successful
                return HttpResponseRedirect(reverse('index'))
            # Else the program will do something here
            # If the account is not active
            else:
                return HttpResponse('Sorry, your account is not active')
        else:
            print('Login failed')
            print('Username: {} and Passord: {}' .format(username, password))
            return HttpResponse("Invalid login datail")
        # iF NOTHING IS SUBMITTED, THIS WILL EXECUTE
    else:
        return render(request, 'basic_app/login.html', {})
