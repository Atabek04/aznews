from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import About_us, WnCards, Followers, Contact, Active_video, HotNews, TrendingArticle


def index(request):
	return render(request, 'index.html')

def about(request):
	about_us = About_us.objects.all()	
	
	context = {
		'about_us': about_us
	}
	return render(request, 'about.html', context)

def blog(request):
	return render(request, 'blog.html')

def category(request):
	cards = WnCards.objects.all()
	followers = Followers.objects.all()
	context = {
		'cards' : cards,
		'followers':followers,
	}
	return render(request, 'category.html', context)

def contact(request):
	contacts = Contact.objects.all()
	hot_news = HotNews.objects.all()
	followers = Followers.objects.all()
	context = {
		'contacts':contacts,
		'hot_news': hot_news,
		'followers':followers,
	}
	return render(request, 'contact.html', context)

def details(request):
	return render(request, 'details.html')

def elements(request):
	return render(request, 'elements.html')

def latest_news(request):
	act_videos = Active_video.objects.all()
	followers = Followers.objects.all()
	hot_news = HotNews.objects.all()
	trend_text = TrendingArticle.objects.all()
	context = {
		'act_videos' : act_videos,
		'followers':followers,
		'hot_news': hot_news,
		'trend_text': trend_text,
	}
	return render(request, 'latest_news.html', context)

def single_blog(request):
	return render(request, 'single-blog.html')