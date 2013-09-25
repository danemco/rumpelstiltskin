from django.contrib import admin

from kaizen.models import Category, Idea, Status, Comment

class CommentInlineAdmin(admin.TabularInline):
    model = Comment
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    pass

class IdeaAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['title', 'body']
    list_display = ('idea', 'category', 'status', 'pub_date',)
    list_filter = ['pub_date', 'status', 'category']

    inlines = [CommentInlineAdmin]

class CommentAdmin(admin.ModelAdmin):
    pass

class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Status, StatusAdmin)
