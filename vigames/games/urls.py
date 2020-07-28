from django.urls import path
from .views import UserProfileDetailView, OutputAllNewsView, GameDetail

urlpatterns = [
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
    path('role/<int:pk>', UserProfileDetailView.as_view(), name="role"),
    path('news/', OutputAllNewsView.as_view(), name="news"),
    path('games/add', GameDetail.as_view(), name="add_game"),
    path('games/<int:pk>/update', GameDetail.as_view(), name="update_game"),
    path('games/<int:pk>/delete', GameDetail.as_view(), name="delete_game"),
    path('games/<int:pk>', GameDetail.as_view(), name="current_game"),
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
