from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import SingleBlog, InstaFeeds, Categories, RecentPost, BlogPost, RecentArticles, WeelkyTopNews2, WeelkyTopNews, TrendRight, TrendTop, TrendBottom, About_us, WnCards, Followers, Contact, Active_video, HotNews, TrendingArticle, Banner
from django.core.paginator import Paginator

def index(request):
	hot_news = HotNews.objects.all()
	cards = WnCards.objects.all()
	followers = Followers.objects.all()
	posters = Banner.objects.all()
	act_videos = Active_video.objects.all()
	trend_bottom = TrendBottom.objects.all()
	trend_top = TrendTop.objects.all()
	trend_right = TrendRight.objects.all()
	top_news = WeelkyTopNews.objects.all()
	top_news2 = WeelkyTopNews2.objects.all()
	recent_articles = RecentArticles.objects.all()

	context = {
		'hot_news':hot_news,
		'cards' : cards,
		'followers':followers,
		'posters':posters,
		'act_videos':act_videos,
		'trend_bottom':trend_bottom,
		'trend_top':trend_top,
		'trend_right':trend_right,
		'top_news':top_news,
		'top_news2':top_news2,
		'recent_articles':recent_articles

	}
	return render(request, 'index.html', context)

def about(request):
	about_us = About_us.objects.all()	
	hot_news = HotNews.objects.all()
	followers = Followers.objects.all()
	posters = Banner.objects.all()
	
	context = {
		'about_us': about_us,
		'hot_news': hot_news,
		'followers':followers,
		'posters':posters,
	}
	return render(request, 'about.html', context)

def blog(request):
	blog_post = BlogPost.objects.all()
	recent_post = RecentPost.objects.all()
	categories = Categories.objects.all()
	instafeeds = InstaFeeds.objects.all()

	context = {
		'blog_post': blog_post,
		'recent_post': recent_post,
		'categories':categories,
		'instafeeds': instafeeds
	}
	return render(request, 'blog.html', context)

def category(request):
	print(request.GET)
	start = 0
	limit = 3
	stop = limit
	
	# Pagination
	current_page = int(float(request.GET.get('page', 1)))
	limit = int(request.GET.get('limit', 3))
	print("current page: ", current_page)

	stop = limit * current_page
	start = stop - limit

	prev_page =  current_page - 1
	next_page = 0

	total = WnCards.objects.count()

	if total > stop:
		next_page = current_page + 1


	card_list = WnCards.objects.all()[start:stop]
	followers = Followers.objects.all()
	posters = Banner.objects.all()
	context = {
		'card_list':card_list,
		'followers':followers,
		'posters':posters,
		'current_page': current_page,
		'prev_page':prev_page,
		'next_page':next_page,
		'limit':limit,

	}
	return render(request, 'category.html', context)

def contact(request):
	contacts = Contact.objects.all()
	context = {
		'contacts':contacts,
	}
	return render(request, 'contact.html', context)

def details(request):
	about_us = About_us.objects.all()
	hot_news = HotNews.objects.all()
	followers = Followers.objects.all()
	posters = Banner.objects.all()

	context = {
		'followers':followers,
		'hot_news': hot_news,
		'about_us': about_us,
		'posters':posters,
	}
	return render(request, 'details.html', context)


def latest_news(request):
	act_videos = Active_video.objects.all()
	followers = Followers.objects.all()
	hot_news = HotNews.objects.all()
	trend_text = TrendingArticle.objects.all()
	posters = Banner.objects.all()
	context = {
		'act_videos' : act_videos,
		'followers':followers,
		'hot_news': hot_news,
		'trend_text': trend_text,
		'posters': posters,
	}
	return render(request, 'latest_news.html', context)

def single_blog(request):
	single_blog = SingleBlog.objects.all()
	instafeeds = InstaFeeds.objects.all()
	categories = Categories.objects.all()

	context = {
		'single_blog':single_blog,
		'instafeeds':instafeeds,
		'categories':categories
	}
	return render(request, 'single-blog.html', context)


def not_found(request, exeption):
	return render(request, '404error.html')

