from django.urls import include, path
from .views import UserProfileDetailView, OutputAllNewsView, GameView, add_game, update_game

urlpatterns = [
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
    path('role/<int:pk>', UserProfileDetailView.as_view(), name="role"),
    path('news/', OutputAllNewsView.as_view(), name="news"),
    path('games/add', add_game, name="add_game"),
    path('games/<int:pk>/update', update_game, name="update_game"),
    path('games/<int:pk>', GameView.as_view(), name="current_game"),
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
