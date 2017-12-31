from django.contrib import admin, messages

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.sitemaps.views import sitemap
from django.forms import TextInput, Textarea
from django.http import HttpResponseNotFound
from django.utils.safestring import mark_safe

from users.models import UserProfile, GuestMessage, UsersMessage, Token, Author, Vip

from django.db import models
from posts.models import Post, Comment, Calender, BankOrders, PhotoAttached


class AdminPost(admin.ModelAdmin):
    exclude = ('author', 'seen',)

    """
        def has_delete_permission(self, request, obj=None):
       
        return False
        
    """

    def save_model(self, request, obj, form, change):
        # obj.public = True
        # if not request.user.is_superuser:
        # obj.public = False

        try:
            if obj.author == request.user.author:
                obj.author = Author.objects.get(user=request.user)
                super(AdminPost, self).save_model(request, obj, form, change)
            elif request.user.is_superuser:
                super(AdminPost, self).save_model(request, obj, form, change)

            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, '.فقط نویسنده این پست میتواند آنرا ویرایش کند')

        except Post.author.RelatedObjectDoesNotExist:
            try:
                obj.author = Author.objects.get(user=request.user)
                super(AdminPost, self).save_model(request, obj, form, change)

            except Author.DoesNotExist:
                messages.set_level(request, messages.ERROR)
                messages.error(request, '.ظاهرا اسم شما در نویسنده ها ثبت نشده است . اینرا به مدیر سایت اطلاع دهید')

        except User.author.RelatedObjectDoesNotExist:
            messages.set_level(request, messages.ERROR)
            messages.error(request, '.ظاهرا اسم شما در نویسنده ها ثبت نشده است . اینرا به مدیر سایت اطلاع دهید')

        except Author.DoesNotExist:
            messages.set_level(request, messages.ERROR)

            messages.error(request, '.ظاهرا اسم شما در نویسنده ها ثبت نشده است . اینرا به مدیر سایت اطلاع دهید')

    def has_delete_permission(self, request, obj=None):
        super(AdminPost, self).has_delete_permission(request, obj=obj)
        if obj is not None:

            if obj.author.user == request.user or request.user.is_superuser:
                return True
            else:
                return False

        else:

            pass


admin.site.register(Post, AdminPost)
admin.site.register(Comment)
admin.site.register(BankOrders)
admin.site.register(Calender)
admin.site.register(PhotoAttached)

admin.site.register(UserProfile)
admin.site.register(GuestMessage)
admin.site.register(UsersMessage)
admin.site.register(Author)
admin.site.register(Vip)

admin.site.register(Token)
