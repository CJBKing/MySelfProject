#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-14 14:05:34
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from django.urls import path
from cms import views

app_name="cms"
urlpatterns=[
	path('',views.index),
	path('login/',views.Login,name="login"),
]