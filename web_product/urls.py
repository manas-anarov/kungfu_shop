from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^list', views.ArticleListView, name='list'),
]