from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/$', views.register, name='register'),
    url(r'login/$', views.login, name='login'),
    url(r'wall/$', views.wall, name='wall'),
    url(r'post_message/$', views.post_message, name='post_message'),
    url(r'post_comment/$', views.post_comment, name='post_comment'),
    url(r'delete_message/(?P<message_id>\d+)/$', views.delete_message, name='delete_message'),
    url(r'logout/$', views.logout, name='logout')
]