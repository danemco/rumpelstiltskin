from django.contrib import admin
from microblog.models import Profile, Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['message']
    date_hierarchy = 'pub_date'
    list_filter    = ['pub_date']
    list_display   = ('profile', 'pub_date', 'message')

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
