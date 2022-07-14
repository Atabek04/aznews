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

admin.site.register(Banner, BannerAdmin),
admin.site.register(WnCards, WnCardsAdmin),
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Followers, FollowersAdmin)