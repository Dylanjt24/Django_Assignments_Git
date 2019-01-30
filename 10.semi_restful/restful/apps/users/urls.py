from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create/$', views.create, name='create'),
    url(r'new/$', views.new, name='new'),
    url(r'show/(?P<user_id>\d+)/$', views.show, name='show'),
    url(r'edit/(?P<user_id>\d+)/$', views.edit, name='edit'),
    url(r'update/(?P<user_id>\d+)/$', views.update, name='update'),
    url(r'delete/(?P<user_id>\d+)/$', views.delete, name='delete')
]