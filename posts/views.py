# -*- coding: utf-8 -*-
from collections import Counter

import pytz
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.timezone import localtime, now
from django.views.generic import ListView
from flask import Flask

from posts.form import CommentForm, CalenderForm
from posts.models import Post, Comment, Calender
from users.forms import UsersContactForm, ContactForm
from users.models import Inbox, Author


def homepage(request):
    # print(localtime(now()) + relativedelta(months=3) > localtime(now()))
    posts_list = Post.objects.all()
    most_seen = Post.objects.order_by("-seen")[:10]


    title = "نوسان صفحه اصلی"
    template_name = 'posts/homepage.html'

    context = {'posts': posts_list, 'most_seen': most_seen, 'title': title}
    return render(request, template_name, context)


def tags(request, tag):
    if request.method == "GET":
        posts_list = Post.objects.all().filter(
            Q(Main_Tag=tag) |

            Q(Tags__icontains=tag)

        )

        paginator = Paginator(posts_list, 1)
        template_name = 'posts/category.html'
        page = request.GET.get('page', 1)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {'posts': posts, 'tag': tag}
        return render(request, template_name, context)


def author(request, author_username):
    author_user_obj = User.objects.get(username=author_username)
    author = Author.objects.get(user=author_user_obj)
    posts_list = Post.objects.filter(author=author)

    paginator = Paginator(posts_list, 1)
    template_name = 'posts/category.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts, }
    print("before return")
    return render(request, template_name, context)


def detail(request, header):
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
                body = str(request.POST.get("body"))
                massage = Inbox.objects.create(user=comment.parent.user, sender=request.user, body=body)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('posts:detail', header=post.header)
    else:
        pre_seen = post.seen

        new_seen = pre_seen + 1

        post.seen = new_seen

        post.save()
        form = CommentForm()
        if request.user.is_authenticated:
            user_prof = request.user.userprofile

            tags_he_saw = user_prof.tags_he_saw
            if Counter(tags_he_saw).get(post.Main_Tag, 0) < 5:
                tags_he_saw.append(post.Main_Tag)
                user_prof.save()

            if len(Counter(tags_he_saw)) > 4:

                tag_should_remove = Counter(tags_he_saw).most_common(4)[3][0]
                tags_he_saw.remove(tag_should_remove)
                user_prof.save()

            elif len(Counter(tags_he_saw)) == 4:

                favourite_tag1 = Counter(tags_he_saw).most_common(4)[0][0]
                favourite_tag2 = Counter(tags_he_saw).most_common(4)[1][0]
                favourite_tag3 = Counter(tags_he_saw).most_common(4)[2][0]
                favourite_tag4 = Counter(tags_he_saw).most_common(4)[3][0]
                favourite_post1 = Post.objects.filter(Main_Tag=favourite_tag1).order_by("-seen")[0]
                favourite_post2 = Post.objects.filter(Main_Tag=favourite_tag2).order_by("-seen")[0]
                favourite_post3 = Post.objects.filter(Main_Tag=favourite_tag3).order_by("-seen")[0]
                favourite_post4 = Post.objects.filter(Main_Tag=favourite_tag4).order_by("-seen")[0]

                context = {'form': form, 'post': post,
                           'favourite_post1': favourite_post1,
                           'favourite_post2': favourite_post2,
                           'favourite_post3': favourite_post3,
                           'favourite_post4': favourite_post4, }
                """
                             favourite_posts = Post.objects.all().filter(

                                 Q(Main_Tag=favourite_tag1) |
                                 Q(Main_Tag=favourite_tag2) |
                                 Q(Main_Tag=favourite_tag3) |
                                 Q(Main_Tag=favourite_tag4) 

                             ).order_by("-seen")[:3]
                             """
                template_name = 'posts/detail.html'
                return render(request, template_name, context)
        template_name = 'posts/detail.html'
        context = {'form': form, 'post': post}
        return render(request, template_name, context)


def search(request):
    template_name = 'posts/category.html'
    queryset_list = None
    query = request.GET.get('q')

    if query:
        queryset_list = Post.objects.all().filter(
            Q(header__icontains=query) |

            Q(Main_Tag__icontains=query) |
            Q(Tags__icontains=query) |
            Q(author__icontains=query)

        )
    context = {'posts': queryset_list, 'tag': query}
    return render(request, template_name, context)


def articles(request, type):
    if type == 'analytical':
        posts_list = Post.objects.filter(is_vip=True, is_article=True)
        title = "مقالات تحلیلی"

    else:
        posts_list = Post.objects.filter(is_vip=False, is_article=True)
        title = "مقالات"

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
    posts_list = Post.objects.filter(is_vip=False, is_article=False)
    title = "اخبار سهام"
    paginator = Paginator(posts_list, 1)
    template_name = 'posts/category.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts, 'title': title}
    return render(request, template_name, context)


def calender(request):
    title = "تقویم اقتصادی"
    template_name = 'specificpages/calender.html'
    return render(request, template_name, {'title': title})


def economic_calender(request):
    queryset_list = None
    query = request.GET.get('q')
    print(query)
    if query:
        queryset_list = Calender.objects.all().filter(
            Q(date__icontains=query)

        )

    template_name = 'specificpages/economic_calender.html'

    context = {'queryset': queryset_list, }
    return render(request, template_name, context)
