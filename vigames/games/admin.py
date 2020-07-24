from django.contrib import admin

from .models import Category, Media, Account, Posts

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Account)
#admin.site.register(Role)
admin.site.register(Media)
