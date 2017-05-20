from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^search_data/$', views.search_data, name='search_data'),
    url(r'^analyse_data/$', views.analyse_data, name='analyse_data'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^logout/$', views.logout, name='logout'),
]