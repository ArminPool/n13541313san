import pytz
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from django.urls import reverse

from users.forms import RegistrationForm, ProfileEditForm, UserEditForm, ResetUserPasswordForm, LoginForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from posts.models import Post

"""
This is what really needs to be explained:
I didn't want to customize django.contrib.auth.User and also i wanted to have phone_number in
registration form and The problem was that there was a field in another form and we haven't a 
UserProfile for user until we create The user.And because of that i first saved user form then 
create a profile for that user and set null=True inside user field in UserProfile Model.

"""


def register(request):
    if request.method == 'POST':

        form1 = RegistrationForm(request.POST)
        form2 = ProfileEditForm(request.POST)

        if form1.is_valid() and form2.is_valid():

            phone_number = form2.cleaned_data['phone_number']
            city = form2.cleaned_data['city']

            user = form1.save()

            UserProfile.create_profile(user, phone_number, city)
            login(request, user)

            return redirect(reverse('posts:home'))

        else:
            print("lvl1")

            form1 = RegistrationForm(request.POST)
            form2 = ProfileEditForm(request.POST)

            args = {'form1': form1, 'form2': form2, }
            return render(request, 'users/reg_form.html', args)
    else:
        form1 = RegistrationForm()
        form2 = ProfileEditForm()
        args = {'form1': form1, 'form2': form2}
        return render(request, 'users/reg_form.html', args)


def login_user(request):
    logout(request)
    username = password = ''

    if request.POST:
        if request.POST['username'] or request.POST['password1']:

            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('posts:home'))
            else:

                return render(request, 'users/login.html',{'error':'نام کاربری یا کلمه ی عبور اشتباه است.'})

        elif request.POST['email'] and not (request.POST['username'] and request.POST['password1']):
            print("email entered")
            return render(request, 'users/login.html', {'done': 'برای شما یک ایمیل حاوی لینک ارسال شده است .'})
    print("requset GET")

    return render(request, 'users/login.html',)


def reset_password_confirm(request):
    if request.POST:
        form = ResetUserPasswordForm(request.POST)

        if form.is_valid():
            password = request.POST['password1']
            user = request.user
            user.set_password(password)
            user.save()
            login(request, user)
            print("changed")
            return render(request, 'users/reset_password_confirm.html', {'message': 'پسورد شما با موفقیت تغییر کرد .'})
    form = ResetUserPasswordForm()
    return render(request, 'users/reset_password_confirm.html', {'form': form})


def logout_user(request):
    user = request.user
    logout(request, user)
    return redirect(reverse('posts:home'))


@login_required
def view_profile(request):
    all_posts = Post.objects.all()
    users = User.objects.get(id=request.user.id)
    try:
        print(request.user)
        print(request.user.userprofile)
        args = {'user': request.user, 'userprofile': request.user.userprofile, 'all_posts': all_posts,
                'timezones': pytz.common_timezones}
        return render(request, 'users/profile.html', args)

    except:

        args = {'user': request.user, 'userprofile': request.user.userprofile, 'users': users, 'all_posts': all_posts,
                'timezones': pytz.common_timezones}
        return render(request, 'users/profile.html', args)


# request.FILES is for save uploaded picture
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profileform = ProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        userform = UserEditForm(request.POST, instance=request.user)

        if profileform.is_valid() and userform.is_valid():
            print("success")
            profileform.save()
            userform.save()
            request.session['django_timezone'] = request.POST['timezone']
            return redirect('/user/profile')

        else:

            args = {'profileform': profileform, 'userform': userform, 'timezones': pytz.common_timezones}
            return render(request, 'users/edit_profile.html', args)
    else:
        profileform = ProfileEditForm(instance=request.user.userprofile)
        userform = UserEditForm(instance=request.user)
        args = {'profileform': profileform, 'userform': userform, 'timezones': pytz.common_timezones}
        return render(request, 'users/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/user/profile')
        else:
            return redirect('/user/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'users/change_password.html', args)
