"""pythonRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapi.api import UserList,UserDetail,UserAuthentication
from testapp import views

from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^userlist/$', UserList.as_view(), name='user_list'),
    url(r'^api/user_list/$',UserList.as_view(),name='user_list'),
    url(r'^api/user_list/(?P<employee_id>\d+)/$', UserDetail.as_view(),name='user_detail'),
    url(r'^api/auth/$',UserAuthentication.as_view(),name='user_authentication'),
    path('',include('testapp.urls'))
    #url(r'^test/$',get_data, name='user_list'),

]


