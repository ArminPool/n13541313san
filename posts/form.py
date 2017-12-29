from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Comment, Calender, PhotoAttached


class PhotoAttachedForm(forms.ModelForm):
    class Meta:
        model = PhotoAttached
        fields = ('author','img', )

# Here I used fields inside The Comment Model Which I created in product/models
# Why I used Only body Field? Cuz We want only Users write Comments under Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CalenderForm(forms.Form):
    my_field = forms.DateField(widget=AdminDateWidget)
