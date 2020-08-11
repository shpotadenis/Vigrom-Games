from django.contrib import admin

from .models import Category, Media, Account, Posts, Comments_Post, Game, FAQ, Genre, Question, Comments_Game, Review, \
    Orders, Views_Game

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(Comments_Post)
admin.site.register(Comments_Game)
admin.site.register(Media)
admin.site.register(Game)
admin.site.register(FAQ)
admin.site.register(Genre)
admin.site.register(Question)
admin.site.register(Review)
admin.site.register(Orders)
admin.site.register(Views_Game)
