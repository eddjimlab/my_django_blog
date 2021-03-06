from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'publish')
    list_per_page = 20


admin.site.register(Post, PostAdmin)
