#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-26 17:58:42
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import xadmin
from . import models
# Register your models here.


class EntryAdmin(object):
	list_display=["title","author","visiting","created_time","modified_time"]

class UserCommentsAdmin(object):
	list_display=["title","email","website","content","created_time",'entry']

xadmin.site.register(models.Category)
xadmin.site.register(models.Tag)
xadmin.site.register(models.Entry,EntryAdmin)
xadmin.site.register(models.UserComment,UserCommentsAdmin)
