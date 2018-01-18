from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect


def specific_pages(request, page):
    if page == "about-us":
        template_name = 'specificpages/about-us.html'
    elif page == "rules":
        template_name = 'specificpages/rules.html'
    elif page == "advertising":
        template_name = 'specificpages/advertising.html'
    elif page == "mql":
        template_name = 'specificpages/mql.html'
    elif page == "pamm":
        template_name = 'specificpages/pamm.html'
    elif page == "tariffs":
        template_name = 'specificpages/tariffs.html'

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(request, template_name)


def tariffs(request):
    if request.user.is_superuser:
        return render(request, 'specificpages/tariffs.html')
    else:
        return render(request,'specificpages/repair.html')