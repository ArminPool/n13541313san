# -*- coding: utf-8 -*-

import pytz
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from django.views.generic import ListView

from posts.form import CommentForm, CalenderForm
from posts.models import Post, Comment, Calender
from users.forms import UsersContactForm, ContactForm
from users.models import Inbox, Author


def homepage(request):
    posts_list = Post.objects.all()
    title = "نوسان صفحه اصلی"
    template_name = 'posts/homepage.html'

    context = {'posts': posts_list, 'title': title}
    return render(request, template_name, context)


def tags(request, tag):
    posts_list = Post.objects.all().filter(
        Q(Main_Tag=tag) |

        Q(Tags__icontains=tag)

    )

    print(posts_list)
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
    print("after posts_list")
    print(posts_list)
    paginator = Paginator(posts_list, 1)
    template_name = 'posts/category.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts,}
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
                print(body)
                massage = Inbox.objects.create(user=comment.parent.user, sender=request.user, body=body)
                print(massage)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', header=post.header)
    else:
        form = CommentForm()
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


