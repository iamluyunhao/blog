from django.conf.urls import url

from backweb import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^art/', views.art, name='art'),
    url(r'^add_art/', views.add_art, name='add_art'),
    url(r'^up_art/(\d+)/', views.up_art, name='up_art'),
    url(r'^del_art/(\d+)/', views.del_art, name='del_art'),
    url(r'^notice/', views.notice, name='notice'),
    url(r'^comment/', views.comment, name='comment'),
    url(r'^category/', views.category, name='category'),
    url(r'^flink/', views.flink, name='flink'),
    url(r'^loginlog/', views.loginlog, name='loginlog'),
    url(r'^manage_user/', views.manage_user, name='manage_user'),
    url(r'^setting/', views.setting, name='setting'),
    url(r'^readset/', views.readset, name='readset'),


]