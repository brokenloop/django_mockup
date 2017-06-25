from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^var/(?P<var>[\w-]+)/$', views.var_input, name='var_input'),
]
