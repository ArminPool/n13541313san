import pytz
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from posts.models import Calender
from users.forms import ContactForm, UsersContactForm


def contact(request):
    users_template_name = 'specificpages/UsersContact.html'
    guest_template_name = 'specificpages/GuestContact.html'
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
    template_name = 'specificpages/about-us.html'
    return render(request, template_name)


def rules(request):
    template_name = 'specificpages/rules.html'
    return render(request, template_name)


def advertising(request):
    template_name = 'specificpages/advertising.html'

    return render(request, template_name)


def mql(request):
    template_name = 'specificpages/mql.html'
    return render(request, template_name)


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
