from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def blog(request):
	return render(request, 'blog.html')

def category(request):
	return render(request, 'category.html')

def contact(request):
	return render(request, 'contact.html')

def details(request):
	return render(request, 'details.html')

def elements(request):
	return render(request, 'elements.html')

def latest_news(request):
	return render(request, 'latest_news.html')

def single_blog(request):
	return render(request, 'single-blog.html')