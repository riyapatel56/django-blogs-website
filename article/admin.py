from django.contrib import admin
from .models import UserModel, ArticleModel, Comment

# Register your models here.
admin.site.register(UserModel)

admin.site.register(ArticleModel)

admin.site.register(Comment)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')