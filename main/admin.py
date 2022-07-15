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

admin.site.register(Banner, BannerAdmin),
admin.site.register(WnCards, WnCardsAdmin),
admin.site.register(Categories, CategoriesAdmin),
admin.site.register(Followers, FollowersAdmin),
admin.site.register(Contact, ContactAdmin)
admin.site.register(Active_video, Active_videoAdmin)
admin.site.register(HotNews, HotNewsAdmin)
admin.site.register(About_us, AboutUsAdmin)
admin.site.register(TrendingArticle, TrendingArticleAdmin)