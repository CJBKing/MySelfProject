#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-02 16:05:35
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from django.conf.urls import url,include

from django.views.generic import TemplateView

from users.views import LoginView
from users.views import RegisterView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView

app_name="users"

urlpatterns=[
    url(r'^index/',TemplateView.as_view(template_name='index.html')),
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    url(r'^forgetpwd/',ForgetPwdView.as_view(),name='forgetpwd'),
    url(r'^reset/(?P<active_code>.*)/',ResetPwdView.as_view(),name="resetPwd"),
    url(r'^modify_pwd/',ModifyPwdView.as_view(),name="modify_pwd"),
]
