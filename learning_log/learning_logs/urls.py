#定义learning_logs的URL模式

from django.urls import path,re_path
from . import views
from .models import Topic
app_name = 'learning_logs'

urlpatterns = [
    #主页
    path('',views.index,name='index'),
    re_path(r'topics/$',views.topics,name='topics'),
    #特定主题
    re_path(r'topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #添加新主题的网页
    re_path(r'new_topic/$',views.new_topic,name='new_topic'),
    #添加新blog
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    #删除blog
    re_path(r'^delete_entry/(?P<entry_id>\d+)$', views.delete_entry, name='delete_entry'),
    #删除主题
    re_path(r'^delete_topic/(?P<topic_id>\d+)$', views.delete_topic, name='delete_topic'),
]