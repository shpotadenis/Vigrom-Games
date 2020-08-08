from datetime import timedelta, date
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .search import Search_engine
from .models import Account, Posts, Game, Review, Category, FAQ, Comments_Post, Comments_Game, Media, Genre
from .serializers import AccountSerializer, OutputAllNews, GameSerializer, OutputPost, \
    ReviewSerializer, CommentsNewsSerializer, PostSerializer, FaqSerializer, CommentsGameSerializer, \
    OrderSerializer, OutputGameSerializer, QuestionSerializer, SerializerMedia, GameLibrarySerializer, GenreSerializer, \
    StatisticsSerializer, OutputReviewSerializer
from django.contrib.auth.models import User
from scripts import Search


class OutputAllNewsView(APIView):
    """Вывод списка последних новостей"""

    def get(self, request):
        news = Posts.objects.filter(draft=False)
        serializer = OutputAllNews(news, many=True)
        return Response(serializer.data)


class AccountDetail(APIView):
    """Получение, редактирование и удаление аккаунта пользователя"""

    def get(self, request):
        user = request.user
        account = Account.objects.get(user=user)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        account = Account.objects.get(user=user)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid() and user.is_authenticated:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        if user.is_authenticated:
                user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostView(APIView):
    """Получение, редактирование и удаление новости"""

    def get(self, request, pk):
        try:
            news = Posts.objects.get(id=pk, draft=False)
            serializer = OutputPost(news)
            return Response(serializer.data)
        except:
            raise Http404

    def post(self, request):
        user = request.user
        serializer = PostSerializer(data=request.data)
        account = Account.objects.get(user=user)
        if serializer.is_valid() and user.is_authenticated and account.is_developer:
            serializer.save(author=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        posts = Posts.objects.get(id=pk)
        serializer = PostSerializer(posts, data=request.data)
        user = request.user
        account = Account.objects.get(user=user)
        if serializer.is_valid() and user.is_authenticated and account.is_developer and posts.author == user:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        posts = Posts.objects.get(id=pk)
        account = Account.objects.get(user=request.user)
        if account.is_developer and posts.user == request.user:
            posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentNewsCreateView(APIView):
    """Добавление комментария на страницу записи"""

    """
    Help text: комментарий оставляет авторизованный пользователь User.
    Оставляет его на странице page. Страницу мы ищем по url страницы, который нам отправит фронт
    Проверяем зарегистрирован ли пользователь и валидный ли комментарий и сохраняем его в базу с соответствующими параметрами
    
    Важно! Если зайти в сериализатор комментария, в него не отправляется Page, 
    т.к. страница у нас определяется по url (то что вверху описано).
    """
    def post(self, request):
        user = request.user
        comment = CommentsNewsSerializer(data=request.data)
        text_comment = Search.comments(Search(), request.data['text_comment'])  # Закрываем матерные слова звездочками
        posts = Posts.objects.get(url=request.data["page"])    # Ищем пост, к которому был оставлен коммент. По урлу.
        if comment.is_valid() and user.is_authenticated:
            comment.save(user=user, page=posts, text_comment=text_comment)
            return Response(comment.data)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment = Comments_Post.objects.get(id=pk)
        serializer = CommentsNewsSerializer(comment, data=request.data)
        text_comment = Search.comments(Search(), request.data['text_comment'])  # Закрываем матерные слова звездочками
        user = request.user
        if serializer.is_valid() and user.is_authenticated and comment.user == user:
            serializer.save(text_comment=text_comment)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comments_Post.objects.get(id=pk)
        if comment.user == request.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentGameCreateView(APIView):
    """Добавление комментария на страницу игры"""

    """
    Help text: комментарий оставляет авторизованный пользователь User.
    Оставляет его на странице game. Страницу мы ищем по url страницы, который нам отправит фронт
    Проверяем зарегистрирован ли пользователь и валидный ли комментарий и сохраняем его в базу с соответствующими параметрами
    
    Важно! Если зайти в сериализатор комментария, в него не отправляется Page, 
    т.к. страница у нас определяется по url (то что вверху описано).
    """
    def post(self, request):
        user = request.user
        comment = CommentsGameSerializer(data=request.data)
        text_comment = Search.comments(Search(), request.data['text_comment'])  # Закрываем матерные слова звездочками
        game = Game.objects.get(url=request.data["page"])    # Ищем пост, к которому был оставлен коммент. По урлу.
        if comment.is_valid() and user.is_authenticated:
            comment.save(user=user, page=game, text_comment=text_comment)
            return Response(comment.data)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment = Comments_Game.objects.get(id=pk)
        serializer = CommentsGameSerializer(comment, data=request.data)
        text_comment = Search.comments(Search(), request.data['text_comment'])  # Закрываем матерные слова звездочками
        user = request.user
        if serializer.is_valid() and user.is_authenticated and comment.user == user:
            serializer.save(text_comment=text_comment)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comments_Game.objects.get(id=pk)
        if comment.user == request.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#class GameDetailView(RetrieveUpdateDestroyAPIView):
#    queryset = Game.objects.all()
#    serializer_class = GameSerializer
#    permission_classes = [IsOwnerProfileOrReadOnly]


class GameDetail(APIView):
    """Добавление, получение, редактирование и удаление игры"""

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def post(self, request):
        user = request.user
        serializer = GameSerializer(data=request.data)
        account = Account.objects.get(user=user)
        medias = []
        for i in list(dict(request.data)['images']):     # Добавление картинок к игре
            if user.is_authenticated and account.is_developer:
                medias.append(Media.objects.create(img=i, author=user))
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid() and user.is_authenticated and account.is_developer:
            serializer.save(author=user, image=medias)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        game = self.get_game(pk)
        serializer = OutputGameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk):
        game = self.get_game(pk)
        serializer = GameSerializer(game, data=request.data)
        user = request.user
        account = Account.objects.get(user=user)
        if serializer.is_valid() and user.is_authenticated and account.is_developer and game.author == user:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        game = self.get_game(pk)
        account = Account.objects.get(user=request.user)
        if account.is_developer and game.author == request.user:
                game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameRatingDetail(APIView):
    """Добавление, получение, редактирование и удаление оценки игры"""

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def rating(self, pk):
        game = self.get_game(pk)
        ratings = Review.objects.filter(game=pk)
        length = len(ratings)
        sum = 0
        res = 0
        if length != 0:
            for r in ratings:
                sum += r.mark
            res = sum / length
        game.rating = res
        game.save()

    def post(self, request, pk):
        user = request.user
        mark = request.POST.get('mark')
        game = self.get_game(pk)
        comment = request.POST.get('comment')
        comment = Search.comments(Search(), comment)
        serializer = ReviewSerializer(data={'author': user, 'mark': mark, 'game': pk, 'comment': comment})
        if serializer.is_valid() and user.is_authenticated and user in game.players.all():
            try:
                user_ratings = Review.objects.get(author=user, game=pk)
            except Review.DoesNotExist:
                serializer.save(author=user)
                self.rating(pk)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            user_ratings = Review.objects.get(game=pk)
            serializer = OutputReviewSerializer(user_ratings)
            return Response(serializer.data)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        game = self.get_game(pk)
        mark = request.POST.get('mark')
        user = request.user
        comment = request.POST.get('comment')
        comment = Search.comments(Search(), comment)
        if user.is_authenticated:
            try:
                user_rating = Review.objects.get(author=user, game=pk)
            except Review.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = ReviewSerializer(user_rating, data={'author': user, 'mark': mark, 'game': pk, 'comment': comment})
            if serializer.is_valid():
                serializer.save(author=user)
                self.rating(pk)
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        if user.is_authenticated:
            try:
                user_ratings = Review.objects.get(author=user, game=pk)
            except Review.DoesNotExist:
                user_ratings = None
            if user_ratings != None:
                user_ratings.delete()
                self.rating(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OutputGames(ListAPIView):
    """Вывод списка игр за неделю"""

    def get(self, request):
        games = Game.objects.filter(date_release__gte=date.today()-timedelta(days=7))\
            .order_by('-date_release')[:10]
        serializer = GameLibrarySerializer(games, many=True)
        return Response(serializer.data)


class BuyGameDetail(APIView):
    """Покупка игры"""

    def post(self, request, pk):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                if user not in game.players.all():
                    game.players.add(user)
                    game.who_added_to_wishlist.remove(user)
                    price = game.price * game.sale_percent / 100
                    game.number_of_players += 1
                    game.save()
                    serializer = OrderSerializer(data={'user': user.id, 'game': pk, 'price': price, 'date': date.today()})
                    if serializer.is_valid():
                        serializer.save()
                    return Response({"message": "success"}, status=status.HTTP_200_OK)
                return Response({"message": "bought"})
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)


class WishListDetail(APIView):
    """Добавление, удаление игры в вишлист"""

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            try:
                games = Game.objects.filter(who_added_to_wishlist=user)
                serializer = GameLibrarySerializer(games)
                return Response(serializer.data)
            except Game.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                if user not in game.who_added_to_wishlist.all():
                    game.who_added_to_wishlist.add(user)
                    return Response({"message": "success"}, status=status.HTTP_200_OK)
                return Response({"message": "added"})
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                if user in game.who_added_to_wishlist.all():
                    game.who_added_to_wishlist.remove(user)
            except Account.DoesNotExist:
                pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssessPostDetail(APIView):
    """Добавление оценки поста, ее удаление"""

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        user = request.user
        post = Posts.objects.get(id=pk)
        if user.is_authenticated:
            try:
                account = Account.objects.get(user=user)
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)
        if request.POST.get('like') == "True":
            if account not in post.liked.all():
                post.liked.add(account)
                if account in post.disliked.all():
                    post.disliked.remove(account)
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        else:
            if account not in post.disliked.all():
                post.disliked.add(account)
                if account in post.liked.all():
                    post.liked.remove(account)
            return Response({"message": "success"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user
        post = Posts.objects.get(id=pk)
        if user.is_authenticated:
            try:
                account = Account.objects.get(user=user)
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)
        if request.POST.get('like') == "True":
            if account in post.liked.all():
                post.liked.remove(account)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            if account in post.disliked.all():
                post.disliked.remove(account)
            return Response(status=status.HTTP_204_NO_CONTENT)


class OutputLibrary(ListAPIView):
    """Вывод библиотеки игр пользователя"""

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            games = Game.objects.filter(players=user)
            serializer = GameLibrarySerializer(games, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class OutputWishlist(ListAPIView):
    """Вывод библиотеки игр пользователя"""

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            games = Game.objects.filter(who_added_to_wishlist=user)
            serializer = GameLibrarySerializer(games, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DownloadGame(ListAPIView):
    """Скачивание игры"""

    def get(self, request, pk):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            #try:
                #account = Account.objects.get(user=user)
                if user in game.players.all():
                    if game.file:
                        response = HttpResponse(game.file)
                        #надо заставлять разрабов загружать только зипы? сохранять имя и тип файла?
                        response['Content-Disposition'] = 'attachment; filename=' + game.title + '.zip'
                        return response
            #except Account.DoesNotExist:
            #    return Response({"message": "fail"})
        return Response({"message": "fail"})


class GameCategoryDetail(ListAPIView):
    """Вывод игр соответствующей категории"""

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        games = Game.objects.filter(categories=category)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class FaqDetail(ListAPIView):
    """Вывод вопросов и ответов"""

    def get(self, request):
        faq = FAQ.objects.all()
        serializer = FaqSerializer(faq, many=True)
        return Response(serializer.data)


class RoleView(APIView):
    """Добавление роли аккуанта"""

    def post(self, request):
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        try:
            is_developer = request.POST.get('is_developer')
            account = Account.objects.get(user=user)
            if is_developer == "true":
                account.is_developer = True
                account.is_player = False
                account.save()
            else:
                account.is_player = True
                account.is_developer = False
                account.save()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """Добавление вопроса к администрации"""

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadMedia(APIView):
    """Добавление медиафайлов"""

    def post(self, request):
        user = request.user
        #serializer = SerializerMedia
        account = Account.objects.get(user=user)
        for i in list(dict(request.data)['img']):
            if user.is_authenticated and account.is_developer:
                Media.objects.create(img=i, author=user)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        img = Media.objects.get(id=pk)
        account = Account.objects.get(user=request.user)
        if account.is_developer and img.author == request.user:
                img.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OutputGenre(ListAPIView):
    """Вывод списка жанров"""

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class OutputStatistics(ListAPIView):
    """Вывод статистики разработчика (игра-рейтинг)"""

    def get(self, request):
        user = request.user
        account = Account.objects.get(user=user)
        games = Game.objects.filter(author=user)
        if user.is_authenticated and account.is_developer:
            serializer = StatisticsSerializer(games, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

'''
class SearchView(APIView):
    """
    Поиск по новостям или играм
    request.data['search'] - текст запроса
    dir - раздел в котором ищем. Может быть двух типов games/news
    user - id пользователя
    """
    def post(self, request):
        user = request.user
        user_id = 0
        if user.is_authenticated:
            user_id = user.id
        if request.data['dir'] == 'news':
            list = Search.search(Search(), request.data['search'], 'news', user_id)
            list_object = [Posts.objects.get(id=i) for i in list]

            print(request.data['search'])
            print(list)
            print(list_object)
            serializer = OutputAllNews(list_object)
            return Response(serializer.data)
        elif request.data['dir'] == 'games':
            list = Search.search(Search(), request.data['search'], 'games', user_id)
            list_object = [Game.objects.get(id=i) for i in list]
            serializer = OutputPost(list_object, many=True)
            print(list_object)
            print(type(list_object))
            #print(type((list_object).json))
            return Response(list_object)
        #else:
            #return Response(status=status.HTTP_204_NO_CONTENT)
'''
class SearchView(APIView):
    """
    Поиск по новостям или играм
    request.data['search'] - текст запроса
    dir - раздел в котором ищем. Может быть двух типов games/news
    user - id пользователя
    """

    def post(self, request):
        text = request.data['search']
        if request.data['dir'] == 'games':
            game = Game.objects.filter()
            serializer = OutputGameSerializer(game, many=True)
        elif request.data['dir'] == 'news':
            post = Posts.objects.filter(draft=False)
            serializer = OutputPost(post, many=True)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        list_index = Search_engine(text, list(serializer.data))
        return Response(list_index)

