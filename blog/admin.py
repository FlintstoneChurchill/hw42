from django.contrib import admin

from blog.models import User, Post, Comment, Mark

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Mark)

