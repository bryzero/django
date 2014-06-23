from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tank.forms import UserForm, UserProfileForm


def index(request):
    return render(request, 'tank/index.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'tank/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tank/')
            else:
                return HttpResponse("Your Langtank account is disabled. You have to log in at least once every 12 months.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'tank/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/tank/')


# @login_required
# def profile_page(request):
    # return render(request, 'tank/index.html', {})


def about(request):
    return render(request, 'tank/about.html', {})


def profile(request):
    return render(request, 'tank/profile.html', {})

def edit_profile(request):
    context = {}
    return render(request, 'tank/edit_profile.html', context)