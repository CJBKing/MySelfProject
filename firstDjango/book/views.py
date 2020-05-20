from django.http import HttpResponse

def book(Request):
	return HttpResponse("book page")

def book_detail(Request,book_id):
	text="您访问的图书ID是:"+book_id
	return HttpResponse(text)

def book_author(Request):
	id=Request.GET.get("id")
	text="作者的ID是：%s"%id
	return HttpResponse(text)