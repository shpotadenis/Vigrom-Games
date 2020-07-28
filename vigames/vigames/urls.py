from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/accounts/', include("games.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('games.urls')),

    #/auth/users/	зарегистрировать нового пользователя
    #/auth/users/me/	получить/обновить зарегистрированного пользователя
    #/auth/jwt/create/	создать JWT-токен, передав действующему пользователю в запросе post эту конечную
    #точку
    #/auth/jwt/refresh/	получить новый JWT-токен
    #/auth//token/login/ получить новый токен, передав действующему пользователю в запросе post
    # эту конечную точку
    #/auth//token/logout/  удалить токен
    #/auth/users/set_password/ смена пароля
    #/auth//users/set_username/ смена username
    #информация о urlах и запросах:
    #https://djoser.readthedocs.io/en/latest/getting_started.html
    #https://djoser.readthedocs.io/en/latest/base_endpoints.html
    #https://djoser.readthedocs.io/en/latest/token_endpoints.html

    # api/ перенаправляет на урлы, указанные в приложении
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
