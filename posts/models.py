from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, DateField, TimeField
from django import forms
from django.core.urlresolvers import reverse
from django_mysql.models import ListTextField


# Create your models here.

class Post(models.Model):

    header = models.CharField(max_length=500)
    img = models.FileField(null=True, blank=True, upload_to='uploaded')
    description = RichTextField(config_name='awesome_ckeditor')
    text = RichTextField(config_name='awesome_ckeditor')

    date_published = models.DateTimeField()
    Main_Tag = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    is_article = models.BooleanField(default=True)
    is_vip = models.BooleanField(default=True)
    public = models.BooleanField(default=False)

    Tags = ListTextField(
        base_field=models.CharField(max_length=20),
        size=3,  # Maximum of 100 ids in list
    )

    class Meta:
        ordering = ['date_published']

    def __str__(self):
        return self.header


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(User, null=True)
    body = models.TextField(max_length=250, null=True)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    parent = models.ForeignKey("self", null=True, blank=True)
    public = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):

        return self.user.username

    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    # is_public for moderation
    def is_public(self):

        if self.public:
            return True
        return False

    def children(self):
        return Comment.objects.filter(parent=self)


class Calender(models.Model):
    date = DateField()
    time = TimeField()
    stock = CharField(max_length=60)
    event = CharField(max_length=60)
    importance = CharField(max_length=60)
    actual = CharField(max_length=60)
    predict = CharField(max_length=60)
    previous = CharField(max_length=60)
