# -*- coding: utf-8 -*-
import os

import pytz
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.timezone import localtime, now

from news.setting.prod import BASE_DIR, MEDIA_ROOT
from users.models import Token
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext, Context

from django.urls import reverse

from users.forms import RegistrationForm, ProfileEditForm, UserEditForm, ResetUserPasswordForm, LoginForm, \
    UsersContactForm, ContactForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from posts.models import Post

from suds.client import Client

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
    next = ''
    if request.GET.get('next'):
        next = request.GET.get('next')
        print(next)

    if request.POST:
        if request.POST['username'] or request.POST['password1']:

            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next != '':
                    return redirect(next)
                else:
                    return redirect(reverse('posts:home'))


            else:

                return render(request, 'users/login.html', {'error': 'نام کاربری یا کلمه ی عبور اشتباه است.'})

        elif request.POST['email'] and not (request.POST['username'] and request.POST['password1']):
            email = request.POST['email']
            try:
                if User.objects.get(email=email):
                    user = User.objects.get(email=email)
                    token = Token.create_and_get_token()
                    plaintext = 'شما برای عوض کردن پسورد خود درخواست داده اید!!!'
                    user_id = user.id
                    context = {'username': user.username, 'token': token, 'user_id': user_id}
                    subject, from_email, to = 'لینک تغییر پسورد', 'support@navasangold.com', email
                    text_content = plaintext
                    html_content = render_to_string('users/reset_password_email.html', context)
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

                    return render(request, 'users/login.html',
                                  {'message': 'برای شما یک ایمیل حاوی لینک ارسال شده است .'})

            except ObjectDoesNotExist:
                return render(request, 'users/login.html', {'message': 'این ایمیل کاربری وجود ندارد.'})

    return render(request, 'users/login.html', )


def reset_password_confirm(request, token, user_id):
    if request.POST:
        form = ResetUserPasswordForm(request.POST)

        if form.is_valid():
            password = request.POST['password1']
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()
            login(request, user)
            return render(request, 'users/reset_password_confirm.html', {'message': 'پسورد شما با موفقیت تغییر کرد .'})

    try:

        token_object = Token.objects.get(token=token)

        form = ResetUserPasswordForm()
        return render(request, 'users/reset_password_confirm.html', {'form': form})
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def logout_user(request):
    user = request.user
    logout(request, user)
    return redirect(reverse('posts:home'))


@login_required
def view_profile(request):
    all_posts = Post.objects.all()
    users = User.objects.get(id=request.user.id)
    try:

        args = {'user': request.user, 'userprofile': request.user.userprofile, 'all_posts': all_posts,
                'timezones': pytz.common_timezones}
        return render(request, 'users/profile.html', args)

    except:

        args = {'user': request.user, 'userprofile': request.user.userprofile, 'users': users, 'all_posts': all_posts,
                'timezones': pytz.common_timezones}
        return render(request, 'users/profile.html', args)


cities = ["آذربایجان شرقی", "آذربایجان غربی", "اصفهان", "اردبیل", "بوشهر", "ایلام", "بوشهر", "تهران",
          "چهارمحال و بختیاری",
          "خراسان جنوبی", "خراسان رضوی", "خراسان شمالی", "خوزستان", "خوزستان", "زنجان",
          "سیستان و بلوچستان", "سمنان", "فارس", "قم", "قزوین", "کهکیلویه و بویراحمد", "کردستان",
          "کرمان", "کرمانشاه", "گیلان", "گلستان", "لرستان", "مازندران", "مرکزی", "هرمزگان", "همدان",
          "یزد"]


# request.FILES is for save uploaded picture
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profileform = ProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        userform = UserEditForm(request.POST, instance=request.user)
        userprofile = request.user.userprofile
        img_name = request.user.userprofile.pro_img.name

        if profileform.is_valid() and userform.is_valid():
            if request.FILES:
                pro_img_directory = MEDIA_ROOT + '/'

                os.remove(pro_img_directory + img_name)

                profileform.save()

                os.rename(pro_img_directory + request.user.userprofile.pro_img.name,
                          pro_img_directory + request.user.username + '.png')

                userprofile.pro_img.name = pro_img_directory + 'uploaded/users/pro_img/' + request.user.username + '.png'
                userprofile.save()
            profileform.save()
            userform.save()
            request.session['django_timezone'] = request.POST['timezone']
            return redirect('/user/profile')

        else:

            args = {'profileform': profileform, 'userform': userform, 'timezones': pytz.common_timezones,
                    'cities': cities}
            return render(request, 'users/edit_profile.html', args)
    else:
        profileform = ProfileEditForm(instance=request.user.userprofile)
        userform = UserEditForm(instance=request.user)
        args = {'profileform': profileform, 'userform': userform, 'timezones': pytz.common_timezones, 'cities': cities}
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


def contact(request):
    users_template_name = 'users/UsersContact.html'
    guest_template_name = 'users/GuestContact.html'
    title = "تماس با ما"
    if request.method == 'POST':

        if request.user.is_authenticated:

            form = UsersContactForm(request.POST)
            if form.is_valid():
                # use print for debugging
                usermassage = form.save(commit=False)
                usermassage.author = request.user
                form.save(commit=True)
                return redirect('posts:home')
            else:

                form = UsersContactForm()
                return render(request, users_template_name, {'title': title})
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('posts:home')
            else:

                form = ContactForm()
                context = {'form': form, 'title': title}
                return render(request, guest_template_name, context)

    else:
        if request.user.is_authenticated:

            form = UsersContactForm()
            context = {'form': form, 'title': title}
            return render(request, users_template_name, context)
        else:

            form = ContactForm()
            context = {'form': form, 'title': title}

            return render(request, guest_template_name, context)


def back_from_zarinpal(user_prof, tariffs_number):
    if tariffs_number == '1':
        vip_until = localtime(now()) + relativedelta(months=1)
        userprofile = user_prof
        userprofile.vip_until = vip_until
        userprofile.save()
    elif tariffs_number == '2':
        vip_until = localtime(now()) + relativedelta(months=3)
        userprofile = user_prof
        userprofile.vip_until = vip_until
        userprofile.save()

    elif tariffs_number == '3':
        vip_until = localtime(now()) + relativedelta(months=6)
        userprofile = user_prof
        userprofile.vip_until = vip_until
        userprofile.save()

    elif tariffs_number == '4':
        vip_until = localtime(now()) + relativedelta(months=12)
        userprofile = user_prof
        userprofile.vip_until = vip_until
        userprofile.save()


MMERCHANT_ID = '07842040-dd2f-11e7-b265-005056a205be'
ZARINPAL_WEBSERVICE = 'https://www.zarinpal.com/pg/services/WebGate/wsdl'


def send_to_zarinpal(request, tariffs_number):
    user = request.user
    email = request.user.email
    mobile = user.userprofile.phone_number
    description = "پرداخت مبلغ اشتراک به سایت نوسان گلد"
    client = Client(ZARINPAL_WEBSERVICE)
    if tariffs_number == "1":

        amount = "1000"
        result = client.service.PaymentRequest(MMERCHANT_ID,
                                               amount,
                                               description,
                                               email,
                                               mobile,
                                               'http://www.navasangold.com/user/verify-after-zarinpal/1/')

        if result.Status == 100:

            return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
        else:
            return 'Error'
    elif tariffs_number == "2":
        amount = "250000"
        result = client.service.PaymentRequest(MMERCHANT_ID,
                                               amount,
                                               description,
                                               email,
                                               mobile,
                                               '/verify/2')
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
        else:
            return 'Error'
    elif tariffs_number == "3":

        amount = "50000"
        result = client.service.PaymentRequest(MMERCHANT_ID,
                                               amount,
                                               description,
                                               email,
                                               mobile,
                                               '/verify/3')
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
        else:
            return 'Error'

    elif tariffs_number == "4":

        amount = "1000000"
        result = client.service.PaymentRequest(MMERCHANT_ID,
                                               amount,
                                               description,
                                               email,
                                               mobile,
                                               '/verify/4')

        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
        else:
            return 'Error'


def verify_after_zarinpal(request, tariffs_number):
    amount = 0
    if tariffs_number == "1":
        amount = "1000"
    elif tariffs_number == "2":

        amount = "250000"
    elif tariffs_number == "3":

        amount = "500000"
    elif tariffs_number == "4":
        amount = "1000000"
    user_prof = request.user.userprofile
    client = Client(ZARINPAL_WEBSERVICE)
    if request.GET.get('Status') == 'OK':
        template_name = 'users/verify_after_zarinpal.html'
        result = client.service.PaymentVerification(MMERCHANT_ID,
                                                    request.GET['Authority'],
                                                    amount)
        if result.Status == 100:
            back_from_zarinpal(user_prof, tariffs_number)
            context = {'refID': str(result.RefID), 'tariffs_number': tariffs_number}
            return render(request, template_name, context)

        elif result.Status == 101:
            return 'Transaction submitted : ' + str(result.Status)
        else:
            return 'Transaction failed. Status: ' + str(result.Status)
    else:
        return 'Transaction failed or canceled by user'
