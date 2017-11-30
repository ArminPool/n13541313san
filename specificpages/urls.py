from django.conf.urls import url

from specificpages.views import mql, contact, about_us, advertising, economic_calender, calender

app_name = 'specificpages'
urlpatterns = [
    url(r'^mql5/$',mql,name="mql"),
    url(r'^contact/$', contact, name='Contact'),
    url(r'^about-us/$', about_us, name='about-us'),
    url(r'^advertising/$', advertising, name='advertising'),
    url(r'^EconomicCalendar/$', economic_calender, name='economic_calendar'),

    url(r'^calender/$', calender, name='calender'),
    # Allows to render our own login page
  ]