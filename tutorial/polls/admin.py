from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceAdmin(admin.ModelAdmin):
    pass

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    list_filter = ['active']
    list_display = ('question', 'pub_date', 'active', 'was_published_recently')
    readonly_fields = ['created']
    fieldsets = (
        (None, {
            'fields': ('question', 'slug', ('pub_date', 'created'),)
         }),
         ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('active',),
         }),
    )

    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)


