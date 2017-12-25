# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
import random
import string
from threading import Timer

import time

import django
from django.contrib.auth.models import User

from django.db import models
from django.utils.timezone import localtime, now
from django_mysql.models import ListTextField


class Inbox(models.Model):
    user = models.ForeignKey(User, default=None, null=True, related_name="message_owner")
    sender = models.ForeignKey(User, default=None, null=True, related_name="message_sender")
    body = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    # Each user-field in UserProfile can only have one user
    user = models.OneToOneField(User, null=True)

    phone_number = models.CharField(max_length=11, blank=False)

    آذربایجان_شرقی = "آذربایجان شرقی"

    آذربایجان_غربی = "آذربایجان غرقی"

    اصفهان = "اصفهان"
    اردبیل = "اردبیل"
    ایلام = "ایلام"
    بوشهر = "بوشهر"
    تهران = "تهران"
    چهارمحال_و_بختیاری = "چهارمحال و بختیاری"

    خراسان_جنوبی = "خراسان جنوبی"
    خراسان_رضوی = "خراسان رضوی"

    خراسان_شمالی = "خراسان شمالی"

    خوزستان = "خوزستان"
    زنجان = "زنجان"
    سیستان_و_بلوچستان = "سیستان و بلوچستان"
    سمنان = "سمنان"
    فارس = "فارس"
    قم = "قم"
    قزوین = "قزوین"
    کهکیلویه_و_بویراحمد = "کهکیلویه و بویراحمد"
    کردستان = "کردستان"
    کرمان = "کرمان"
    کرمانشاه = "کرمانشاه"
    گیلان = "گیلان"
    گلستان = "گلستان"
    لرستان = "لرستان"
    مازندران = "مازندران"
    مرکزی = "مرکزی"
    هرمزگان = "هرمزگان"
    همدان = "همدان"
    یزد = "یزد"

    cities = ((آذربایجان_شرقی, 'آذربایجان شرقی'),
              (آذربایجان_غربی, "آذربایجان غربی"),
              (اصفهان, "اصفهان"
               ),
              (اردبیل, "اردبیل"),
              (ایلام, "ایلام"),
              (بوشهر, "بوشهر"),
              (تهران, "تهران"
               ),
              (چهارمحال_و_بختیاری, "چهارمحال_و_بختیاری"
               ),
              (خراسان_جنوبی, "خراسان_جنوبی"
               ),
              (خراسان_رضوی, "خراسان_رضوی"
               ),
              (خراسان_شمالی, "خراسان_شمالی"
               ),
              (خوزستان, "خوزستان"
               ),
              (زنجان, "زنجان"
               ),
              (سیستان_و_بلوچستان, "سیستان_و_بلوچستان"
               ),
              (سمنان, "سمنان"
               ),
              (فارس, "فارس"
               ),
              (قم, "قم"
               ),
              (قزوین, "قزوین"
               ),
              (کهکیلویه_و_بویراحمد, "کهکیلویه_و_بویراحمد"
               ),
              (کردستان, "کردستان"
               ),
              (کرمان, "کرمان"
               ),
              (کرمانشاه, "کرمانشاه"
               ),
              (گیلان, "گیلان"
               ),
              (گلستان, "گلستان"
               ),
              (لرستان, "لرستان"
               ),
              (مازندران, "مازندران"
               ),
              (مرکزی, "مرکزی"
               ),
              (هرمزگان, "هرمزگان"
               ),
              (همدان, "همدان"
               ),
              (یزد, "یزد"
               )

              )
    tags_he_saw = ListTextField(
        base_field=models.CharField(max_length=20),
        size=80,
        blank=True)
    city = models.CharField(choices=cities, max_length=25, default='tehran')
    pro_img = ProcessedImageField(upload_to='uploaded/users/pro_img',

                                  format='JPEG',
                                  options={'quality': 60}, null=True, blank=True)

    vip_until = models.DateTimeField(default=django.utils.timezone.now)
    # Remember Many to Many fields doesn't show in mysql commend line
    inbox = models.ManyToManyField(Inbox, blank=True)

    def __str__(self):
        if self.user:
            return self.user.username
        return "unknown"

    def have_vip(self):
        return self.vip_until > localtime(now())

    @classmethod
    def create_profile(cls, user, phone_number, city):
        userprofile = cls.objects.create(

            user=user
        )
        userprofile.phone_number = phone_number
        userprofile.city = city

        userprofile.save()


class Author(models.Model):
    user = models.OneToOneField(User, null=False)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username


"""
Note: Receiver of UsersMessage and GuestMessage is admin  cuz we don't need chat between users 

"""


# Here is Contact for Guest that i said before
class UsersMessage(models.Model):
    sender = models.OneToOneField(User, related_name="sender", null=True, blank=True)

    cooperate = 'co'
    problem_buying = 'pb'
    ask_game = 'ag'
    others = 'o'

    options = (
        (cooperate, 'همکاری'), (problem_buying, 'مشکل در خرید'), (ask_game, 'درخواست بازی'), (others, 'موارد دیگر'))
    issue_options = models.CharField(choices=options, default=cooperate, max_length=2)
    message = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.sender) + " " + str(self.issue_options)


# Here is Contact for Guest that i said before
class GuestMessage(models.Model):
    Guest_first_name = models.CharField(max_length=10, null=True)

    Guest_last_name = models.CharField(max_length=10, null=True)
    Guest_email = models.EmailField(max_length=50, null=True)
    cooperate = 'co'
    problem_buying = 'pb'
    ask_game = 'ag'
    others = 'o'

    options = (
        (cooperate, 'همکاری'), (problem_buying, 'مشکل در خرید'), (ask_game, 'درخواست بازی'), (others, 'موارد دیگر'))
    issue_options = models.CharField(choices=options, default=cooperate, max_length=2)
    message = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.Guest_first_name) + " " + str(self.issue_options)


class Token(models.Model):
    token = models.CharField(max_length=60)
    time_created = models.TimeField(auto_now_add=True)
    expire_time = models.IntegerField(default=180)

    @staticmethod
    def parse_to_sec(time):
        return time.hour * 3600 + time.minute * 60 + time.second

    @classmethod
    def create_and_get_token(cls):
        token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(40))

        token_obj = cls.objects.create(token=token, )
        token_obj.save()
        Timer(600, lambda: cls.delete_token(token_obj)).start()

        return token

    @staticmethod
    def delete_token(token_obj):
        token_obj.delete()


class Vip(models.Model):
    user = models.CharField(default='',max_length=50,blank=False,null=False)
    date_and_time = models.DateTimeField(default=django.utils.timezone.now,blank=False,null=False)
    product = models.CharField(default='',max_length=50,blank=False,null=False)
    amount = models.CharField(default='0تومان',max_length=50,blank=False,null=False)

    def __str__(self):
        return self.user + ' ' + self.product + ' ' + str(self.date_and_time)

    @classmethod
    def add_vip(cls, username, product,amount):
        cls.objects.create(

            user=username
            , product=product
            , date_and_time=localtime(now())
            ,amount=amount
        )
