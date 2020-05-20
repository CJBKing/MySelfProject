#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-14 14:05:19
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from django.urls import path
from front import views
app_name="front"
urlpatterns=[
	path('',views.index),
	path('signin/',views.Login,name="login"),
]
