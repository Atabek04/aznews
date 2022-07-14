from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('blog/', views.blog, name='blog'),
	path('category/', views.category, name='category'),
	path('contact/', views.contact, name='contact'),
	path('details/', views.details, name='details'),
	path('elements/', views.elements, name='elements'),
	path('latest_news/', views.latest_news, name='latest_news'),
	path('single-blog/', views.single_blog, name='single-blog'),
	
]