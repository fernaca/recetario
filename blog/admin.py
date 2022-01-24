from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
