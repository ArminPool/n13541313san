# -*- coding: utf-8 -*-
import datetime

from dateutil.parser import parse
from django.utils import timezone

import dateutil
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.timezone import localtime, now

register = template.Library()


@register.filter(name='persian_numeric')
@stringfilter
def persian_numeric(value):
    length = len(value)
    for char in value:
        if char is '0':
            char = '۰'
            value += char
        elif char is '1':
            char = '۱'
            value += char
        elif char is '2':
            char = '۲'
            value += char
        elif char is '3':
            char = '۳'
            value += char
        elif char is '4':
            char = '۴'
            value += char
        elif char is '5':
            char = '۵'
            value += char
        elif char is '6':
            char = '۶'
            value += char
        elif char is '7':
            char = '۷'
            value += char
        elif char is '8':
            char = '۸'
            value += char
        elif char is '9':
            char = '۹'
            value += char
        else:
            value += char

    return value[length:]


@register.filter(name='fix_spaces')
@stringfilter
def fix_spaces(str):
    fixed_str = str.replace(' ', '-')

    return fixed_str


@register.filter(name='reached_time_published')
@stringfilter
def reached_time_published(date_published_str):
    date_published = parse(date_published_str)
    return localtime(now()) >= date_published
