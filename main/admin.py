from django.contrib import admin
from main.models import *

class BannerAdmin(admin.ModelAdmin):
	pass

class WnCardsAdmin(admin.ModelAdmin):
	pass

class CategoriesAdmin(admin.ModelAdmin):
	pass

class FollowersAdmin(admin.ModelAdmin):
	pass

class ContactAdmin(admin.ModelAdmin):
	pass

class Active_videoAdmin(admin.ModelAdmin):
	pass

class HotNewsAdmin(admin.ModelAdmin):
	pass

class AboutUsAdmin(admin.ModelAdmin):
	pass

class TrendingArticleAdmin(admin.ModelAdmin):
	pass
PersonalQuote
class TrendBottomAdmin(admin.ModelAdmin):
	pass

class TrendTopAdmin(admin.ModelAdmin):
	pass

class TrendRightAdmin(admin.ModelAdmin):
	pass

class WeelkyTopNewsAdmin(admin.ModelAdmin):
	pass

class WeelkyTopNews2Admin(admin.ModelAdmin):
	pass

class RecentArticlesAdmin(admin.ModelAdmin):
	pass

class BlogPostAdmin(admin.ModelAdmin):
	pass

class RecentPostAdmin(admin.ModelAdmin):
	pass

class InstaFeedsAdmin(admin.ModelAdmin):
	pass

class SingleBlogAdmin(admin.ModelAdmin):
	pass

class PersonalQuoteAdmin(admin.ModelAdmin):
	pass


admin.site.register(Banner, BannerAdmin),
admin.site.register(WnCards, WnCardsAdmin),
admin.site.register(Categories, CategoriesAdmin),
admin.site.register(Followers, FollowersAdmin),
admin.site.register(Contact, ContactAdmin)
admin.site.register(Active_video, Active_videoAdmin)
admin.site.register(HotNews, HotNewsAdmin)
admin.site.register(About_us, AboutUsAdmin)
admin.site.register(TrendingArticle, TrendingArticleAdmin)
admin.site.register(TrendBottom, TrendBottomAdmin)
admin.site.register(TrendTop, TrendTopAdmin)
admin.site.register(TrendRight, TrendRightAdmin)
admin.site.register(WeelkyTopNews, WeelkyTopNewsAdmin)
admin.site.register(WeelkyTopNews2, WeelkyTopNews2Admin)
admin.site.register(RecentArticles, RecentArticlesAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(RecentPost, RecentPostAdmin)
admin.site.register(InstaFeeds, InstaFeedsAdmin)
admin.site.register(SingleBlog, SingleBlogAdmin)