from django.shortcuts import render
from django.contrib.auth import authenticate,login

from django.contrib.auth.backends import ModelBackend  # 让用户可以通过邮箱或者用户名都可以登录，
#用自定义authenticate方法,这里是继承ModelBackend类来做的验证
from .models import UserProfile,EmailVerifyRecord
from django.db.models import Q

from django.views.generic.base import View

from .forms import LoginForm,RegisterForm,ForgetPwdForm,ModifyPwdForm#表单验证
from django.contrib.auth.hashers import make_password #密码加密
from utils.email_send import send_register_email
# Create your views here.
#邮箱和用户名都可以登录
#基础ModelBackend类，因为他有authenticate方法
class CustomBackend(ModelBackend):
	def authenticate(self,request,username=None,password=None,**kwargs):
		try:
			#不希望用户存在两个，get只能有一个，两个get是失败的一种原因，Q为使用并集查询
			user=UserProfile.Objects.get(Q(username=username)|Q(email=username))

			#django的后台中密码加密：所以不能password==password
			#UserProfile继承的AbstractUser中有def check_password(self,raw_password):
			if user.check_password(password):
				return user
		except Exception as e:
			return None




class LoginView(View):
		def get(self,request):
			return render(request,'login.html')

		def post(self,request):
			#实例化
			login_form=LoginForm(request.POST)
			if login_form.is_valid():
				#获取用户提交的用户名和密码
				user_name=request.POST.get('username',None)
				pass_word=request.POST.get('password',None)
				#成功返回user对象，失败返回None
				user=authenticate(username=user_name,password=pass_word)
				#如果不是null说明验证成功
				if user is not None:
					#登录
					if user.is_active: #只有注册激活才能登录
						login(request,user)
						return render(request,'blog/index.html')
				else:	#只有当用户名或密码不存在时，才返回错误信息到前端
					return render(request,'login.html',{'msg':'用户名或密码错误','login_form':login_form})
			else:	#form.is_valid()已经判断不合法了，所以这里不需要再返回错误信息到前端了
				return render(request,'login.html',{'login_form':login_form})


#激活用户
class ActiveUserView(View):
		def get(self,request,active_code):
			#查询邮箱验证记录是否存在
			all_record=EmailVerifyRecord.objects.filter(code=active_code)

			if all_record:
				for record in all_record:
					#获取到对应的邮箱
					email=record.email
					#查找到邮箱对应的user
					user=UserProfile.objects.get(email=email)
					user.is_active=True
					user.save()
					#激活成功跳转到登陆页面
					return render(request,"login.html")
			else:  #验证码不对的时候跳转到激活失败的页面
				return render(request,'register.html',{'msg':"您的激活链接无效"})



class RegisterView(View):
		#用户注册
		def get(self,request):
			register_form=RegisterForm()
			return render(request,'register.html',{'register_form':register_form})

		def post(self,request):
			register_form=RegisterForm(request.POST)
			if register_form.is_valid():
				user_name=request.POST.get('email',None)
				pass_word=request.POST.get("password",None)
				#如果用户已经存在，则提示错误信息
				if UserProfile.objects.filter(email=user_name):
					return render(request,"register.html",{'register_form':register_form,'msg':'用户已经存在'})


				#实例化一个user_profile对象
				user_profile=UserProfile()
				user_profile.username=user_name
				user_profile.email=user_name
				user_profile.is_active=False
				#对保存到数据库的密码加密
				user_profile.password=make_password(pass_word)
				user_profile.save()
				send_register_email(user_name,'register')
				return render(request,'login.html')
			else:
				return render(request,'register.html',{'register_form':register_form})



#忘记密码
class ForgetPwdView(View):
		def get(self,request):
			forget_form=ForgetPwdForm()
			return render(request,"forgetpwd.html",{"forget_form":forget_form})

		def post(self,request):
			forget_form=ForgetPwdForm(request.POST)
			if forget_form.is_valid():
				email=request.POST.get("email",None)
				send_register_email(email,'forget')
				return render(request,'send_success.html')
			else:
				return render(request,'forgetpwd.html',{"forget_form":forget_form})


#点击重置密码验证链接，如果验证通过跳转修改密码页面
class ResetPwdView(View):
		def get(self,request,active_code):
			all_records=EmailVerifyRecord.objects.filter(code=active_code)
			if all_records:
				for record in all_records:
					email=record.email
					return render(request,"password_reset.html",{"email":email})
			else:
				return render(request,"active_fail.html")
			return render(request,"login.html")


#修改密码
class ModifyPwdView(View):
	def post(self,request):
		modify_form=ModifyPwdForm(request.POST)
		if modify_form.is_valid():
			pwd1=request.POST.get("password1","")
			pwd2=request.POST.get("password2","")
			email=request.POST.get("email","")
			if pwd1!=pwd2:
				return render(request,"password_reset.html",{"email":email,"msg":"密码不一致"})
			user=UserProfile.objects.get(email=email)
			user.password=make_password(pwd2)
			user.save()

			return render(request,"login.html")
		else:
			email=request.POST.get("email","")
			return render(request,"password_reset.html",{"email":email,"modify_form":modify_form})