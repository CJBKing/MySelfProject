from django.shortcuts import render

# Create your views here.

def index(Request):
	return render(Request,"index.html")

def add_book(Request):
	context={
		"content":"添加图书页"
	}
	return render(Request,"add_book.html",context)


def book_detail(Request,book_id):
	pass

