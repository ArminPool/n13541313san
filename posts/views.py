# -*- coding: utf-8 -*-

import pytz
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from django.views.generic import ListView

from posts.form import CommentForm, CalenderForm
from posts.models import Post, Comment, Calender
from users.forms import UsersContactForm, ContactForm
from users.models import Inbox


def homepage(request):
    posts_list = Post.objects.all()
    title = "نوسان صفحه اصلی"
    template_name = 'posts/homepage.html'
    send_mail(
        'Subject here',
        'Here is the message.',
        'support@navasangold.com',
        ['armin.oldboy@gmail.com'],
        fail_silently=False,
    )
    print(1)
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


def author(request, author):
    posts_list = Post.objects.filter(author=author)

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
    context = {'posts': posts, 'tag': author}
    return render(request, template_name, context)


def contact(request):
    users_template_name = 'users/UsersContact.html'
    guest_template_name = 'users/GuestContact.html'
    title = "تماس با ما"
    if request.method == 'POST':

        if request.user.is_authenticated:

            form = UsersContactForm(request.POST)
            if form.is_valid():
                # use print for debugging
                usermassage = form.save(commit=False)
                usermassage.author = request.user
                form.save(commit=True)
                return redirect('posts:home')
            else:
                print('invalid-users-form')

                print('authenticated')
                form = UsersContactForm()
                return render(request, users_template_name, {'title': title})
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('posts:home')
            else:

                form = ContactForm()
                context = {'form': form, 'title': title}
                return render(request, guest_template_name, context)

    else:
        if request.user.is_authenticated:

            form = UsersContactForm()
            context = {'form': form, 'title': title}
            return render(request, users_template_name, context)
        else:

            form = ContactForm()
            context = {'form': form, 'title': title}

            return render(request, guest_template_name, context)


def about_us(request):
    template_name = 'posts/about-us.html'
    return render(request, template_name)


def advertising(request):
    template_name = 'posts/advertising.html'

    return render(request, template_name)


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


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'posts/timezone.html', {'timezones': pytz.common_timezones})


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
    template_name = 'posts/calender.html'
    return render(request, template_name, {'title': title})


def economic_calender(request):
    queryset_list = None
    query = request.GET.get('q')
    print(query)
    if query:
        queryset_list = Calender.objects.all().filter(
            Q(date__icontains=query)

        )

    template_name = 'posts/economic_calender.html'

    context = {'queryset': queryset_list, }
    return render(request, template_name, context)
