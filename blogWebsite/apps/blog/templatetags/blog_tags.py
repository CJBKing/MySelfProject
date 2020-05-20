#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-25 15:17:45
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django import template
from ..models import Entry,Category,Tag

register=template.Library()

#文章总数
@register.simple_tag
def get_total_entrycount():
	return Entry.objects.all().count()
# 最新文章
@register.simple_tag
def get_recent_entries(num=5):
	return Entry.objects.all().order_by('-created_time')[:num]

# 热门文章
@register.simple_tag
def get_popular_entries(num=5):
	return Entry.objects.all().order_by('-visiting')[:num]


# 分类
@register.simple_tag
def get_categories():
	return Category.objects.all()


@register.simple_tag
def get_entry_count_of_category(category_name):
	return Entry.objects.filter(category__name=category_name).count()

# 归档
@register.simple_tag
def archives():
	return Entry.objects.dates("created_time",'month',order="DESC")

@register.simple_tag
def get_entry_count_of_date(year,month):
	return Entry.objects.filter(created_time__year=year,created_time__month=month).count()

# 标签
@register.simple_tag
def get_tags():
	return Tag.objects.all()