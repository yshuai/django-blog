from django.conf.urls import  url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
#第一个参数是网址，第二个参数是处理函数，name将作为处理函数 index 的别名
