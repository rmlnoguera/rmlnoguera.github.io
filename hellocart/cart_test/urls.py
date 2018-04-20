from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from cart_test import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^carts/$', views.CartList.as_view()),
    url(r'^carts/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^cartitems/$', views.CartItemList.as_view()),
    url(r'^cartitems/(?P<pk>[0-9]+)/$', views.CartItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)