#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-26 20:38:50
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django import forms
from captcha.fields import CaptchaField

#登录表单验证
class LoginForm(forms.Form):
	#用户名密码不能为空
	username=forms.CharField(required=True,min_length=5)
	password=forms.CharField(required=True,min_length=5)


#注册验证表单
class RegisterForm(forms.Form):
	email=forms.EmailField(label=("email"),required=True,min_length=5)
	password=forms.CharField(label=("password"),required=True,min_length=5)
	#验证码,字段里面可以自定义错误提示信息
	captcha=CaptchaField(label=("captcha"),error_messages={'invalid':'验证码错误'})


#忘记密码表单验证
class ForgetPwdForm(forms.Form):
	email=forms.EmailField(required=True)
	captcha=CaptchaField(error_messages={'invalid':"验证码错误"})

#修改密码的form表单
class ModifyPwdForm(forms.Form):
	"""重置密码"""
	password1=forms.CharField(required=True,min_length=5)
	password2=forms.CharField(required=True,min_length=5)