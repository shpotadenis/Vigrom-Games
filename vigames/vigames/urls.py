from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/accounts/', include("games.urls")),
    path('api-auth/', include('rest_framework.urls')),


    #/auth/users/	зарегистрировать нового пользователя
    #/auth/users/me/	получить/обновить зарегистрированного пользователя
    #/auth/jwt/create/	создать JWT, передав действующему пользователю в запросе post эту конечную
    #точку
    #/auth/jwt/refresh/	получить новый JWT

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
