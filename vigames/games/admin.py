from django.contrib import admin

from .models import Category, Media, Account, Posts, Comments_Post, Game, FAQ

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(Comments_Post)
#admin.site.register(Role)
admin.site.register(Media)
admin.site.register(Game)
admin.site.register(FAQ)