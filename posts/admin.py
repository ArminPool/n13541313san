from django.contrib import admin

# Register your models here.
from django.contrib.sitemaps.views import sitemap
from django.forms import TextInput, Textarea

from users.models import UserProfile, GuestMessage, UsersMessage, Inbox, Token, Author, Vip

from django.db import models
from posts.models import Post, Comment, Calender, BankOrders


class AdminModel(admin.ModelAdmin):
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        # obj.public = True
        # if not request.user.is_superuser:

        # obj.public = False
        obj.author = Author.objects.get(user=request.user)
        super(AdminModel, self).save_model(request, obj, form, change)


admin.site.register(Post,AdminModel)
admin.site.register(Comment)
admin.site.register(BankOrders)
admin.site.register(Calender)
admin.site.register(UserProfile)
admin.site.register(Inbox)
admin.site.register(GuestMessage)
admin.site.register(UsersMessage)
admin.site.register(Author)
admin.site.register(Vip)

admin.site.register(Token)
