#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-22 18:41:08
# @Author  : jinbo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import xadmin
from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
	#显示Course表的字段列
	list_display=['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
	#搜索字段
	search_fields=['name','degree','add_time']

	#过滤
	list_filter=['name','degree','learn_times','students','fav_nums','image','click_nums','add_time']

xadmin.site.register(Course,CourseAdmin)

class LessonAdmin(object):
	list_display=['course','name','add_time']

	search_fields=['course','name','add_time']
	#这里course__name是根据课程名称过滤
	list_filter=['course__name','name','add_time']

xadmin.site.register(Lesson,LessonAdmin)

class VideoAdmin(object):
	list_display=['lesson','name','add_time']

	search_fields=['lesson','name']

	list_filter=['lesson','name','add_time']

xadmin.site.register(Video,VideoAdmin)


class CourseResourceAdmin(object):
	list_display=['course','name','download','add_time']
	search_fields=['course__name','name']
	list_filter=['course__name','name','add_time']

xadmin.site.register(CourseResource,CourseResourceAdmin)