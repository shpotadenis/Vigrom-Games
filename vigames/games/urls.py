from django.urls import path
from .views import AccountDetail, OutputAllNewsView, GameDetail, OutputGames, \
    GameRatingDetail, BuyGameDetail, WishListDetail, AssessPostDetail, OutputLibrary, DownloadGame,\
    PostView, GameCategoryDetail, CommentNewsCreateView, CommentGameCreateView, FaqDetail, DownloadMedia

urlpatterns = [
    path('', OutputGames.as_view(), name="main"),

    path('profile/<str:pk>', AccountDetail.as_view(), name="profile"),
    path('profile/<str:pk>/library', OutputLibrary.as_view(), name="library"),

    #path('role/<int:pk>', UserProfileDetailView.as_view(), name="role"),

    path('games/add', GameDetail.as_view(), name="add_game"),
    path('games/<int:pk>', GameDetail.as_view(), name="current_game"),
    path('games/<int:pk>/update', GameDetail.as_view(), name="update_game"),
    path('games/<int:pk>/delete', GameDetail.as_view(), name="delete_game"),
    path('games/<int:pk>/rating', GameRatingDetail.as_view(), name="rating_game"),
    path('games/<int:pk>/buy', BuyGameDetail.as_view(), name="buy_game"),
    path('games/<int:pk>/download', DownloadGame.as_view(), name="download_game"),
    path('games/<int:pk>/wishlist', WishListDetail.as_view(), name="wishlist"),

    path('news/add', PostView.as_view(), name="add_new_post"),
    path('news/<int:pk>/assess', AssessPostDetail.as_view(), name="assess"),
    path('news/<str:pk>/', PostView.as_view(), name='view_post'),
    path('news/<int:pk>/update', PostView.as_view(), name='update_post'),
    path('news/<int:pk>/delete', PostView.as_view(), name='delete_post'),
    path('news/', OutputAllNewsView.as_view()),

    path('categories/<str:pk>', GameCategoryDetail.as_view(), name="assess"),

    path('faq', FaqDetail.as_view(), name="faq"),

    path('commentnews/add', CommentNewsCreateView.as_view(), name="add_new_comment_news"),
    path('commentnews/<int:pk>/update', CommentNewsCreateView.as_view(), name="update_new_comment_news"),
    path('commentnews/<int:pk>/delete', CommentNewsCreateView.as_view(), name="delete_new_comment_news"),

    path('commentgame/add', CommentGameCreateView.as_view(), name="add_new_comment_game"),
    path('commentgame/<int:pk>/update', CommentGameCreateView.as_view(), name="update_new_comment_game"),
    path('commentgame/<int:pk>/delete', CommentGameCreateView.as_view(), name="delete_new_comment_game"),

    path('uploads/add', DownloadMedia.as_view(), name='download_media')
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
