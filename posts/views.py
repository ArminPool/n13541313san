# -*- coding: utf-8 -*-
import urllib.parse
from collections import Counter

import pytz
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from datetime import datetime

from django.http import HttpResponseNotFound, JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.timezone import localtime, now
from django.views import View
from django.views.generic import ListView
from flask import Flask

from posts.form import CommentForm, CalenderForm, PhotoAttachedForm
from posts.models import Post, Comment, Calender, BankOrders, PhotoAttached, Signal
from users.forms import UsersContactForm, ContactForm
from users.models import Author


def homepage(request):
    # print(localtime(now()) + relativedelta(months=3) > localtime(now()))
    title = 'نوسان گلد | صفحه اصلی'
    template_name = 'posts/homepage.html'
    posts_list = Post.objects.filter(public=True)
    most_seen = Post.objects.order_by("-seen")[:10]

    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'most_seen': most_seen, 'title': title}
    return render(request, template_name, context)


def tags(request, tag):

    if request.method == "GET":
        tag = urllib.parse.unquote(tag).replace('-', ' ')

        posts_list = Post.objects.all().filter(
            Q(Main_Tag=tag) |

            Q(Tags__icontains=tag)

        )
        most_seen = Post.objects.order_by("-seen")[:10]

        paginator = Paginator(posts_list, 6)
        template_name = 'posts/category.html'
        page = request.GET.get('page', 1)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {'posts': posts, 'tag': tag,'most_seen':most_seen}
        return render(request, template_name, context)


def author(request, author_username):
    author_user_obj = User.objects.get(username=author_username)
    author = Author.objects.get(user=author_user_obj)
    posts_list = Post.objects.filter(author=author)
    most_seen = Post.objects.order_by("-seen")[:10]


    paginator = Paginator(posts_list, 6)
    template_name = 'posts/category.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts,'most_seen':most_seen }
    return render(request, template_name, context)


def detail(request, header):
    header = urllib.parse.unquote(header).replace('-', ' ')
    post = Post.objects.get(header=header)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            try:
                parent_id = int(request.POST.get("parent_id"))

            except:
                parent_id = None

            if parent_id:
                comment.parent = Comment.objects.get(pk=parent_id)

            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('posts:detail', header=post.header)

    elif not request.user.is_authenticated and post.is_vip:

        return render(request, 'posts/no_vip.html')

    elif request.user.is_authenticated and post.is_vip and not request.user.userprofile.have_vip():

        return render(request, 'posts/no_vip.html')

    else:

        pre_seen = post.seen

        new_seen = pre_seen + 1

        post.seen = new_seen

        post.save()
        form = CommentForm()
        if request.user.is_authenticated:
            context = {'form': form, 'post': post}
            user_prof = request.user.userprofile

            tags_he_saw = user_prof.tags_he_saw

            if Counter(tags_he_saw).get(post.Main_Tag, 0) < 5:
                tags_he_saw.append(post.Main_Tag)
                user_prof.save()

            if len(Counter(tags_he_saw)) > 4:

                if Counter(tags_he_saw).most_common(5)[4][0] == post.Main_Tag:

                    tag_should_remove = Counter(tags_he_saw).most_common(5)[3][0]
                else:
                    tag_should_remove = Counter(tags_he_saw).most_common(5)[4][0]

                tags_he_saw.remove(tag_should_remove)
                user_prof.save()

                context = {'form': form, 'post': post}

            if len(Counter(tags_he_saw)) == 4:
                show = True
                favourite_tag1 = Counter(tags_he_saw).most_common(4)[0][0]
                favourite_tag2 = Counter(tags_he_saw).most_common(4)[1][0]
                favourite_tag3 = Counter(tags_he_saw).most_common(4)[2][0]
                favourite_tag4 = Counter(tags_he_saw).most_common(4)[3][0]

                try:
                    favourite_post1 = Post.objects.filter(Main_Tag=favourite_tag1).order_by("-seen")[0]
                except IndexError:
                    tags_he_saw.remove(favourite_tag1)
                    user_prof.save()
                    show = False
                try:
                    favourite_post2 = Post.objects.filter(Main_Tag=favourite_tag2).order_by("-seen")[0]
                except IndexError:
                    tags_he_saw.remove(favourite_tag2)
                    user_prof.save()
                    show = False
                try:
                    favourite_post3 = Post.objects.filter(Main_Tag=favourite_tag3).order_by("-seen")[0]
                except IndexError:
                    tags_he_saw.remove(favourite_tag3)
                    user_prof.save()
                    show = False
                try:
                    favourite_post4 = Post.objects.filter(Main_Tag=favourite_tag4).order_by("-seen")[0]
                except IndexError:
                    tags_he_saw.remove(favourite_tag4)
                    user_prof.save()
                    show = False
                if show:
                    context = {'form': form, 'post': post,
                               'favourite_post1': favourite_post1,
                               'favourite_post2': favourite_post2,
                               'favourite_post3': favourite_post3,
                               'favourite_post4': favourite_post4, }

                else:
                    context = {'form': form, 'post': post}

            template_name = 'posts/detail.html'
            return render(request, template_name, context)

    template_name = 'posts/detail.html'
    context = {'form': form, 'post': post}
    return render(request, template_name, context)


def search(request):
    template_name = 'posts/category.html'
    queryset_list = None
    query = request.GET.get('q')
    most_seen = Post.objects.order_by("-seen")[:10]

    if query:
        queryset_list = Post.objects.all().filter(
            Q(header__icontains=query) |
            Q(analysis_branch__icontains=query) |
            Q(analysis_subcategory__icontains=query) |
            Q(Main_Tag__icontains=query) |
            Q(Tags__icontains=query)

        )
    context = {'posts': queryset_list, 'tag': query, 'most_seen': most_seen}
    return render(request, template_name, context)


def articles(request, find):
    title, posts_list = '', ''
    if find == 'regular':
        posts_list = Post.objects.filter(post_type='article')
        title = "مقالات"

    if find == 'price-action-uo':
        posts_list = Post.objects.filter(analysis_subcategory='price_action', analysis_branch='universal_ons')
        title = "انس جهانی | تحلیلات پرایس اکشن"

    elif find == 'elliott-uo':
        posts_list = Post.objects.filter(analysis_subcategory='elliott', analysis_branch='universal_ons')
        title = "انس جهانی | تحلیلات الیوت"

    elif find == 'ichimoku-uo':
        posts_list = Post.objects.filter(analysis_subcategory='ichimoku', analysis_branch='universal_ons')
        title = "انس جهانی | تحلیلات ایچی موکو"

    elif find == 'price-action-poc':
        posts_list = Post.objects.filter(analysis_subcategory='price_action', analysis_branch='pairs_of_currencies')
        title = "جفت ارزها | تحلیلات پرایس اکشن"

    elif find == 'elliott-poc':
        posts_list = Post.objects.filter(analysis_subcategory='elliott', analysis_branch='pairs_of_currencies')
        title = "جفت ارزها | تحلیلات الیوت"

    elif find == 'ichimoku-poc':
        posts_list = Post.objects.filter(analysis_subcategory='ichimoku', analysis_branch='pairs_of_currencies')
        title = "جفت ارزها | تحلیلات ایچی موکو"

    elif find == 'domestic-dollar':
        posts_list = Post.objects.filter(analysis_branch='domestic_dollar')
        title = "تحلیلات دلار داخلی"

    paginator = Paginator(posts_list, 6)
    template_name = 'posts/homepage.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts, 'title': title}
    return render(request, template_name, context)


def news(request):
    posts_list = Post.objects.filter(is_vip=False, post_type='news')
    most_seen = Post.objects.order_by("-seen")[:10]

    title = "اخبار"
    paginator = Paginator(posts_list, 6)
    template_name = 'posts/category.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        # ---- we mention to title as tag in category template and in this case ----
    context = {'posts': posts, 'most_seen': most_seen, 'tag': title}
    return render(request, template_name, context)


def calender(request):
    title = "تقویم اقتصادی"
    template_name = 'posts/calender.html'

    return render(request, template_name, {'title': title})


def economic_calender(request):
    queryset_list = None

    query = urllib.parse.unquote(request.GET.get('q'))
    if query:
        queryset_list = Calender.objects.all().filter(
            Q(date__icontains=query)

        )

    template_name = 'posts/economic_calender.html'

    context = {'queryset': queryset_list, }
    return render(request, template_name, context)


def bank_orders(request):
    template_name = 'posts/bankorders.html'
    if not request.user.is_authenticated:

        return render(request, 'posts/no_vip.html')

    elif not request.user.userprofile.have_vip():

        return render(request, 'posts/no_vip.html')
    else:
        query_list = BankOrders.objects.all()
        context = {'query_list': query_list}

        return render(request, template_name, context)


def upload_photo_affiliate(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.user.userprofile.is_author:
                form = PhotoAttachedForm()
                author = Author.objects.get(user=request.user)

                photos_list = PhotoAttached.objects.filter(author=author)
                context = {'photos': photos_list, 'form': form}
                return render(request, 'posts/upload-photo-affiliate.html', context, )
            else:
                return HttpResponseForbidden('<h1>not allowed</h1>')
        else:
            return HttpResponseForbidden('<h1>not allowed</h1>')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.userprofile.is_author:

                form = PhotoAttachedForm(request.POST, request.FILES)
                if form.is_valid():
                    photo = form.save(commit=False)
                    author = Author.objects.get(user=request.user)

                    photo.author = author
                    photo.save()
                    data = {'is_valid': True, 'name': photo.img.name, 'url': photo.img.url,
                            'uploaded_at': photo.uploaded_at}
                else:
                    data = {'is_valid': False}
                return JsonResponse(data)
            else:
                return HttpResponseForbidden('<h1>not allowed</h1>')
        else:
            return HttpResponseForbidden('<h1>not allowed</h1>')


def signals(request):
    template_name = 'posts/signals.html'
    if not request.user.is_authenticated:

        return render(request, 'posts/no_vip.html')

    elif not request.user.userprofile.have_vip():

        return render(request, 'posts/no_vip.html')
    else:
        query_list = Signal.objects.all()
        context = {'query_list': query_list}

        return render(request, template_name, context)
