from django.urls import path
from .views import AccountDetail, OutputAllNewsView, GameDetail, OutputGames, \
    GameRatingDetail, BuyGameDetail, WishListDetail, AssessPostDetail, OutputLibrary, DownloadGame, \
    PostView, GameCategoryDetail, CommentNewsCreateView, CommentGameCreateView, FaqDetail, RoleView, \
    QuestionDetail, DownloadMedia, OutputStatistics, OutputWishlist, SearchView, OutputGenreGames, \
    OutputGenreTopGames, HideGameDetail, ShowGameDetail, GameInfoToEditDetail, RecommendedGamesDetail, \
    BestGamesDetail

urlpatterns = [
    path('main/new', OutputGames.as_view(), name="main"),
    path('main/recommended', RecommendedGamesDetail.as_view(), name="recommended_games"),
    path('main/best', BestGamesDetail.as_view(), name="best_games"),

    path('profile', AccountDetail.as_view(), name="profile"),
    path('profile/library', OutputLibrary.as_view(), name="library"),
    path('profile/wishlist', OutputWishlist.as_view(), name="profile_wishlist"),
    #path('profile/statistics', OutputStatistics.as_view(), name="statistics"),
    path('profile/statistics/', OutputStatistics.as_view(), name="statistics"),
    path('profile/statistics/<int:pk>', OutputStatistics.as_view(), name="statistics"),

    path('role', RoleView.as_view(), name="role"),

    #path('genres', OutputGenre.as_view(), name="genres"),

    path('games/add', GameDetail.as_view(), name="add_game"),
    path('games/<int:pk>', GameDetail.as_view(), name="current_game"),
    path('games/<int:pk>/update', GameDetail.as_view(), name="update_game"),
    path('games/<int:pk>/delete', GameDetail.as_view(), name="delete_game"),
    path('games/<int:pk>/rating', GameRatingDetail.as_view(), name="rating_game"),
    path('games/<int:pk>/buy', BuyGameDetail.as_view(), name="buy_game"),
    path('games/<int:pk>/download', DownloadGame.as_view(), name="download_game"),
    path('games/<int:pk>/wishlist', WishListDetail.as_view(), name="wishlist"),
    path('games/<int:pk>/hide', HideGameDetail.as_view(), name="hide_game"),
    path('games/<int:pk>/show', ShowGameDetail.as_view(), name="show_game"),
    path('games/<int:pk>/show_info', GameInfoToEditDetail.as_view(), name="show_game_info_to_edit"),

    path('genre/<str:pk>', OutputGenreGames.as_view(), name="genre_games"),
    path('genre/<str:pk>/top', OutputGenreTopGames.as_view(), name="genre_top_games"),

    path('news/', OutputAllNewsView.as_view()),
    path('news/add', PostView.as_view(), name="add_new_post"),
    path('news/<int:pk>/assess', AssessPostDetail.as_view(), name="assess"),
    path('news/<int:pk>/', PostView.as_view(), name='view_post'),
    path('news/<int:pk>/update', PostView.as_view(), name='update_post'),
    path('news/<int:pk>/delete', PostView.as_view(), name='delete_post'),

    path('categories/<int:pk>', GameCategoryDetail.as_view(), name="assess"),

    path('faq', FaqDetail.as_view(), name="faq"),

    path('question', QuestionDetail.as_view(), name="question"),

    path('commentnews/add', CommentNewsCreateView.as_view(), name="add_new_comment_news"),
    path('commentnews/<int:pk>/update', CommentNewsCreateView.as_view(), name="update_new_comment_news"),
    path('commentnews/<int:pk>/delete', CommentNewsCreateView.as_view(), name="delete_new_comment_news"),

    path('commentgame/add', CommentGameCreateView.as_view(), name="add_new_comment_game"),
    path('commentgame/<int:pk>/update', CommentGameCreateView.as_view(), name="update_new_comment_game"),
    path('commentgame/<int:pk>/delete', CommentGameCreateView.as_view(), name="delete_new_comment_game"),

    path('uploads/add', DownloadMedia.as_view(), name='upload_media'),
    path('uploads/<int:pk>/delete', DownloadMedia.as_view(), name='delete_media'),

    path('search', SearchView.as_view(), name='search'),
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
