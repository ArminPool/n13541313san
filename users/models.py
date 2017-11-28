# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models


class Inbox(models.Model):
    user = models.ForeignKey(User, null=True, related_name="message_owner")
    sender = models.ForeignKey(User, null=True, related_name="message_sender")
    body = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    # Each user-field in UserProfile can only have one user
    user = models.OneToOneField(User, null=True)

    phone_number = models.CharField(max_length=11, blank=False)

    azar_sharghi = "آذربایجان شرقی"

    azar_gharbi = "آذربایجان غربی"

    اصفهان = "اصفهان"
    اردبیل = "اردبیل"
    ایلام = "ایلام"
    بوشهر = "بوشهر"
    تهران = "تهران"
    چهارمحال_و_بختیاری = "چهارمحال و بختیاری"

    خراسان_جنوبی = "خراسان جنوبی"
    خراسان_رضوی = "خراسان_رضوی"

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

    cities = ((آذربایجان_شرقی, 'آذربایجان'),
              (آذربایجان_غربی, "آذربایجان"),
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

    city = models.CharField(choices=cities,max_length=25, default='tehran')
    pro_img = models.FileField(null=True, blank=True, upload_to='uploaded')
    inbox = models.ManyToManyField(Inbox)
    vip = models.BooleanField(default=False)

    def __str__(self):

        if self.user:
            return self.user.username
        return "unknown"

    def have_vip(self):

        if self.vip:
            return True
        return False

    @classmethod
    def create_profile(cls, user, phone_number,city):
        userprofile = cls.objects.create(

            user=user
        )
        userprofile.phone_number = phone_number
        userprofile.city = city

        userprofile.save()


"""
Note: Receiver of UsersMessage and GuestMessage is admin  cuz we don't need chat between users in a shop 

"""


# Here is Contact for Guest that i said before
class UsersMessage(models.Model):
    author = models.OneToOneField(User, related_name="author", null=True, blank=True)

    cooperate = 'co'
    problem_buying = 'pb'
    ask_game = 'ag'
    others = 'o'

    options = (
        (cooperate, 'همکاری'), (problem_buying, 'مشکل در خرید'), (ask_game, 'درخواست بازی'), (others, 'موارد دیگر'))
    issue_options = models.CharField(choices=options, default=cooperate, max_length=2)
    message = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.author) + " " + str(self.issue_options)


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
