from django.contrib import admin
from .models import Link, Comment


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display=['title', 'url']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['commented_on', 'commented_by']
# Register your models here.
