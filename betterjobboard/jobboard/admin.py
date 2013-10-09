from django.contrib import admin
from jobboard.models import Profile, Post, Subscriber

class ProfileAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class SubscriberAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ('name', 'email', 'subscribe_date', )
    list_filter = ['subscribe_date']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
