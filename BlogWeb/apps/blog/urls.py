#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-19 17:10:30
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django.conf.urls import url

from . import views

app_name="blog"

urlpatterns=[
	url(r'^$',views.index,name='blog_index'),
	url(r'^(?P<blog_id>[0-9]+)/$',views.detail,name="blog_detail"),
	url(r'^category/(?P<category_id>[0-9]+)/$',views.catagory,name="blog_category"),
	url(r'^tag/(?P<tag_id>[0-9]+)/$',views.tag,name="blog_tag"),
	url(r'^search/$',views.search,name='blog_search'),
	url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$',views.archives,name='blog_archives'),
	url(r'^comments/(?P<blog_id>[0-9]+)/$',views.submit_comment,name="comments"),
]
