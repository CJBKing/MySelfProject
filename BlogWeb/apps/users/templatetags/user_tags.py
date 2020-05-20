#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-27 11:02:04
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from django import template
from ..models import UserProfile

register=template.Library()


#当前登录的用户信息
@register.simple_tag
def get_userInfo_name():
	return UserProfile.objects.count()