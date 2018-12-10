from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from web import views

router = SimpleRouter()

router.register('art', views.ArticleView)

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^list/', views.list, name='list'),
    url('^category_list/(\d+)/', views.category_list, name='category_list'),
    url(r'^about/', views.about, name='about'),
    url(r'^info/(\d+)/', views.info, name='info'),
]

urlpatterns += router.urls