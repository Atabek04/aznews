from email.mime import image
from statistics import mode
from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField


# ================ Category Page ======================

class Categories(models.Model):
	category = models.CharField(max_length=200)

	def __str__(self):
		return self.category



class Banner(models.Model):
	image = models.ImageField(blank = True, null = True)
	
class WnCards(models.Model):
	image = models.ImageField(blank=True)
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

class Followers(models.Model):
	facebook = models.IntegerField(blank=True)
	link_facebook = models.CharField(max_length=200, null=True, blank=True)
	# --------------------------------------
	instagram = models.IntegerField(blank=True)
	link_instagram = models.CharField(max_length=200, null=True, blank=True)
	# --------------------------------------
	twitter = models.IntegerField(blank=True)
	link_twitter = models.CharField(max_length=200, null=True, blank=True)
	# --------------------------------------
	youtube = models.IntegerField(blank=True)
	link_youtube = models.CharField(max_length=200, null=True, blank=True)

	msg = "Don't create another object, just edit!"
	def __str__(self):
		return self.msg
# ====================================================

# ================ Contact Page ======================
class Contact(models.Model):
	state = models.CharField(max_length=200)
	street = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	
	msg = "Don't create another object, just edit!"
	def __str__(self):
		return self.msg
# ====================================================

# ================ Latest_news Page ======================
class Active_video(models.Model):
	source = models.CharField(max_length=500)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=400)

	def __str__(self):
		return self.title

class HotNews(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title


class TrendingArticle(models.Model):
	title = models.CharField(max_length=200)
	paragraph = models.TextField(max_length=800)
	image = models.ImageField(null= True, blank=True)


	msg = "Don't create another object, just edit!"
	def __str__(self):
		return self.msg
# ====================================================


# ================ About Page ======================
class About_us(models.Model):
	image = models.ImageField(blank=True,null=True)
	description = models.CharField(max_length=400, null=True)
	paragraph = models.TextField(max_length=1500, null=True)

	msg = "Don't create another object, just edit!"
	def __str__(self):
		return self.msg
# ====================================================

# ================ Index Page ========================
class TrendTop(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)

	def __str__(self):
		return self.title


class TrendBottom(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)

	def __str__(self):
		return self.title

class TrendRight(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)

	def __str__(self):
		return self.title


class WeelkyTopNews(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)

	def __str__(self):
		return self.title

class WeelkyTopNews2(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)
	date = models.DateField()

	def __str__(self):
		return self.title

class RecentArticles(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)

	def __str__(self):
		return self.title
# ====================================================

# ================ Blog Page =========================
class BlogPost(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	image = models.ImageField(blank = True, null = True)
	date = models.DateTimeField(auto_now_add=True)
	# comments

	def monthpublished(self):
		return self.date.strftime('%B')

	def daypublished(self):
		return self.date.strftime('%d')

class RecentPost(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(blank = True, null = True)
	date = models.DateTimeField(auto_now_add=True)

class InstaFeeds(models.Model):
	image = models.ImageField(blank = True, null = True)

# ====================================================

# ================ Single-Blog Page =========================
class SingleBlog(models.Model):
	image = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	text1 = models.TextField(max_length=800)
	text2 = models.TextField(max_length=800)
	blockquote = models.TextField(max_length=400)

	