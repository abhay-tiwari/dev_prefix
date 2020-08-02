from django.contrib import admin

from .models import Blog, Category, Comment

admin.site.register(Blog)
admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, query_set):
        query_set.update(active = True)
