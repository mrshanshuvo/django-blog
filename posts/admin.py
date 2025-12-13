from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'post_title', 'published_data']
  list_display_links = ['id', 'post_title']
  list_filter = ['published_data']
  search_fields = ['post_title']
