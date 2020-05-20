"""StudyOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView

from users.views import LoginView
from users.views import RegisterView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView
from organization.views import OrgView

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/',TemplateView.as_view(template_name='index.html')),
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    url(r'^forgetpwd/',ForgetPwdView.as_view(),name='forgetpwd'),
    url(r'^reset/(?P<active_code>.*)/',ResetPwdView.as_view(),name="resetPwd"),
    url(r'^modify_pwd/',ModifyPwdView.as_view(),name="modify_pwd"),
    url(r'^org_list/',OrgView.as_view(),name="org_list"),
]
