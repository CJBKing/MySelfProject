from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# def index(Request):
# 	return HttpResponse("前端首页")

def index(Request):
	username=Request.GET.get('username')
	if username:
		return HttpResponse("前端首页")
	else:
		login_url=reverse("front:login")#login是url的name=【】参数，front为urls中的app_name命名空间，防止反转到其他Url中的名为login的url中
		print(login_url)
		return redirect(login_url)

def Login(Request):
	return HttpResponse("前端登录")