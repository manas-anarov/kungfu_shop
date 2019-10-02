from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	ListView,
	DeleteView
)
from web_product.models import Product
# from .forms import ArticleModelForm


class ArticleListView(ListView):
	template_name = 'article_list.html'
	queryset = Product.objects.all()

