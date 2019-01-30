from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buy/(?P<product_id>\d+)/$', views.buy, name='buy'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^clear/$', views.clear, name='clear')
]