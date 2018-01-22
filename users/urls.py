from django.conf.urls import url
from django.contrib.auth.views import logout
import posts
from users.views import logout_user, send_to_zarinpal, verify_after_zarinpal
from . import views

from posts import views as PV

app_name = 'user'
urlpatterns = [
    url(r'^$', PV.homepage),

    # Allows to render our own login page
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', logout_user),
    url(r'register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

    url(r'^reset-password/confirm/(?P<token>[^/]+)/(?P<user_id>[0-9]+)/$',
        views.reset_password_confirm, name='password_reset_confirm'),

    url(r'^send-to-zarinpal/(?P<tariff_number>[1-4](?![\w\s,?!]))/$',send_to_zarinpal,name='send_to_zarinpal'),
    url(r'^verify-after-zarinpal/(?P<user_id>[1-9]+)/(?P<tariff_number>[1-4](?![\w\s,?!]))/', verify_after_zarinpal, name='verify_after_zarinpal'),

]
