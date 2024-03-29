from django.contrib import admin
from blogmania.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.post.through
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    list_filter = ['active', 'pub_date']
    list_display = ('title', 'pub_date', 'active', 'author')
    fieldsets = (
        (None, {
            'fields' : ('author', 'title', 'body', ('pub_date', 'active'),),
        }),
    )

    inlines = [CategoryInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
