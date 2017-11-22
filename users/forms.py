import re

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile, UsersMessage, GuestMessage


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:  # Define meta data that is related to the class I am inside of
        model = User
        # Here we specify which field we want from UserCreationForm
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        }

    # Here is what we did :Customize  Customize  Customize Cuz the main problem is errors should be Persian

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        try:
            if not username or not email or not first_name or not last_name:
                print("Nothing entered")
                self.add_error(None, 'لطفا تمام  فیلد ها را پر کنید!')
            elif User.objects.get(username=username):
                print("user found")
                self.add_error('username', 'این نام کاربری وجود دارد.')

        except User.DoesNotExist:
            try:
                if User.objects.get(email=email):
                    print("email found")
                    self.add_error('email', 'این ایمیل قبلا استفاده شده !!!')
            except User.DoesNotExist:

                if len(password1) < 8:
                    print("less than 8")
                    self.add_error('password1', 'تعداد  حروف رمز باید بیشتر از 8 باشد.')

                elif password2 != password1:
                    print("dismatch")
                    self.add_error('password1', 'تکرار رمز عبور اشتباه است')


def save(self, commit=True, ):
    user = super(RegistrationForm, self).save(commit=False)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.email = self.cleaned_data['email']

    if commit:
        user.save()

    return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {

            'first_name',
            'last_name',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {

            'pro_img',
            'city',
            'phone_number',

        }

    def clean(self):
        cleaned_data = super(ProfileEditForm, self).clean()
        city = cleaned_data.get('city')
        pro_img = cleaned_data.get('pro_img')
        print(city)
        website = cleaned_data.get('website')
        phone_number = cleaned_data.get('phone_number')
        regex = r'0\d{10}'
        print('form2 lvl1')
        if phone_number is None:
            self.add_error(None, 'لطفا شماره تلفن خود را وارد کنید!')
        elif not re.match(regex, phone_number):
            self.add_error('phone_number', 'شماره تلفن درست وارد نشده!!!')
            print('form2 lvl2')

        if city is None:
            self.add_error(None, 'لطفا استان خود را انتخاب کنید!')
            print("city incorrect")


class ContactForm(forms.ModelForm):
    class Meta:  # Define meta data that is related to the class I am inside of
        model = GuestMessage
        # Here we specify which field we want from UserCreationForm
        fields = {
            'Guest_first_name',
            'Guest_last_name',
            'Guest_email',
            'issue_options',
            'message',
        }


class UsersContactForm(forms.ModelForm):
    class Meta:  # Define meta data that is related to the class I am inside of
        model = UsersMessage
        # Here we specify which field we want from UserCreationForm
        fields = {

            'author',
            'issue_options',
            'message',
        }


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = {

            'username',
            'password1',

        }

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password1')
        print("clean")
        try:
            if not username or not password:
                print("error")
                self.add_error(None, 'لطفا تمام  فیلد ها را پر کنید!')
        except:
            print("except")




class ResetUserPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = {

            'password1',
            'password2',

        }
