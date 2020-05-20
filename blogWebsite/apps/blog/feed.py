#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-25 17:39:49
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from django.contrib.syndication.views import Feed

from .models import Entry

class LatestEntriesFeed(Feed):
	title="博客"
	link="/blogWebsite/"
	description="最新博客文章"

	def items(self):
		return Entry.objects.order_by('-created_time')[:5]

	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return item.abstract