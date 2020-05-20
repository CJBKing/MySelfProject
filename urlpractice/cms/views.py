from django.http import HttpResponse

def index(Request):
	return HttpResponse("CMS首页")


def Login(Request):
	return HttpResponse("CMS登录")