from django.contrib import admin

from .models import Blog, Comment, UserProfile, User, Friend

# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.unregister(User)
admin.site.register(UserProfile)
admin.site.register(Friend)