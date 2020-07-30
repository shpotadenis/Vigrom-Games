from django.urls import path
from .views import UserProfileDetailView, OutputAllNewsView, GameDetail, OutputPostView, OutputGames, CommentCreateView, \
    GameRatingDetail, BuyGameDetail, WishListDetail, AssessPostDetail

urlpatterns = [
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
    path('role/<int:pk>', UserProfileDetailView.as_view(), name="role"),
    path('games/add', GameDetail.as_view(), name="add_game"),
    path('games/<int:pk>/update', GameDetail.as_view(), name="update_game"),
    path('games/<int:pk>/delete', GameDetail.as_view(), name="delete_game"),
    path('games/<int:pk>/rating', GameRatingDetail.as_view(), name="rating_game"),
    path('games/<int:pk>', GameDetail.as_view(), name="current_game"),
    path('games/<int:pk>/buy', BuyGameDetail.as_view(), name="buy_game"),
    path('games/<int:pk>/wishlist', WishListDetail.as_view(), name="wishlist"),
    path('news/', OutputAllNewsView.as_view()),
    path('news/<int:pk>/assess', AssessPostDetail.as_view(), name="assess"),
    path(('news/<str:pk>/'), OutputPostView.as_view()),
    path('', OutputGames.as_view(), name="main"),
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
