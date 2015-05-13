# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from yonetim import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sehirrehberim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','yonetim.views.yonetim'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page':'/accounts/login/'}),
    url(r'^yonetim/$','yonetim.views.yonetim'),
    url(r'^accounts/register/$','yonetim.views.register'),
    url(r'^kampanya-ekle/$','yonetim.views.kampanya_ekleme'),
    url(r'^kampanya-listesi/$','yonetim.views.kampanya_listesi'),
    url(r'^kampanyalar/$', views.kampanya_list),
    url(r'^kampanyalar/(?P<pk>[0-9]+)/$', views.kampanya_detail),
    )
