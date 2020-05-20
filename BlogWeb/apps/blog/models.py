from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from users.models import UserProfile
# Create your models here.

class Category(models.Model):
	name=models.CharField('分类',max_length=128)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name="博客分类"
		verbose_name_plural=verbose_name



class Tag(models.Model):
	name=models.CharField('标签',max_length=128)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name="博客标签"
		verbose_name_plural=verbose_name


class Entry(models.Model):
	articleChoice=(
		("originNew","原创"),
		("otherOld","转载"),
		)
	title=models.CharField("文章标题",max_length=128)
	author=models.ForeignKey(UserProfile,verbose_name="作者",on_delete=models.CASCADE)
	img=models.ImageField(upload_to="blog_img",null=True,blank=True,verbose_name="博客配图")
	body=models.TextField("正文")
	abstract=models.TextField("摘要",max_length=256,null=True,blank=True)
	visiting=models.PositiveIntegerField("访问量",default=0)
	category=models.ManyToManyField("Category",verbose_name="博客分类")
	tags=models.ManyToManyField("Tag",verbose_name="标签")
	created_time=models.DateTimeField("创建时间",auto_now_add=True)
	modified_time=models.DateTimeField("修改时间",auto_now=True)
	article_type=models.CharField("文章类型",max_length=20,choices=articleChoice,default="originNew")
	def __str__(self):
		return self.title


	class Meta:
		ordering=['-created_time']
		verbose_name="博客正文"
		verbose_name_plural=verbose_name

	def get_articleType():
		return """articleChoice[self.article_type]"""
	def get_absolute_url(self):
		#获取当前博客详情URL
		return reverse("blog:blog_detail",kwargs={"blog_id":self.id}) #app名字，详情页url的别名，参数是当前博客的id

	def increase_visiting(self):
		#访问量加一
		self.visiting+=1
		self.save(update_fields=['visiting'])  #只保存某个字段


class UserComment(models.Model):
	title=models.CharField(verbose_name="评论标题",max_length=20)
	email=models.EmailField(verbose_name="邮箱",max_length=50)
	website=models.URLField(blank=True)
	content=models.TextField(verbose_name='评论内容')
	created_time=models.DateTimeField(auto_now_add=True)

	entry=models.ForeignKey(Entry) #一篇文章多个评论
	# comment_user=models.ForeignKey(UserProfile)
	class Meta:
		verbose_name="用户评论"
		verbose_name_plural=verbose_name