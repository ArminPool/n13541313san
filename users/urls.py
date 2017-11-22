from django.conf.urls import url

import posts
from users.views import logout_user
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

    url(r'^reset-password/confirm/$',
        views.reset_password_confirm, name='password_reset_confirm'),

]
