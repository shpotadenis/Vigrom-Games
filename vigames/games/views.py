from datetime import timedelta, date
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .search import Search_engine
from .models import Account, Posts, Game, Review, Category, FAQ, Comments_Post, Comments_Game, Media, Genre, Orders, \
    Views_Game
from .serializers import AccountSerializer, OutputAllNews, GameSerializer, OutputPost, \
    ReviewSerializer, CommentsNewsSerializer, PostSerializer, FaqSerializer, CommentsGameSerializer, \
    OrderSerializer, OutputGameSerializer, QuestionSerializer, SerializerMedia, OutputShortGameInfoSerializer, \
    GenreSerializer, \
    StatisticsSerializer, OutputReviewSerializer, OutputGameInfoToEditSerializer, OutputDevelopersGamesInfoSerializer
from django.contrib.auth.models import User
from scripts import Search
from collections import OrderedDict

class OutputAllNewsView(APIView):
    """Вывод списка последних новостей"""

    def get(self, request):
        news = Posts.objects.filter(draft=False)
        serializer = OutputAllNews(news, many=True)
        # Получаем избранные записи. Сортируем по дате и выбираем последние 4 записи
        news_fav = Posts.objects.filter(draft=False, fav=True, ).order_by('-fav_date', '-num_views')[:4]
        serializer_fav = OutputAllNews(news_fav, many=True)
        return Response({'news_fav': list(serializer_fav.data), 'news': list(serializer.data)})


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
            post = Posts.objects.get(id=pk, draft=False)
            serializer = OutputPost(post)
            post.num_views += 1     # Увеличиваем счетчик просмотров на 1
            post.save()
            print(serializer.data)
            for i in range(len(serializer.data['comments_post'])):
                user = User.objects.get(username=serializer.data['comments_post'][i]['user'])
                # Отдельный комментарий преобразуем в словарь. затем добавляем в него аватар по модели юзера
                serializer.data['comments_post'][i] = dict(serializer.data['comments_post'][i])
                try:
                    serializer.data['comments_post'][i]['avatar'] = Account.objects.get(user=user).avatar.url
                except:
                    serializer.data['comments_post'][i]['avatar'] = 'None'

                for ch in range(len(serializer.data['comments_post'][i]['children_post'])):
                    user = User.objects.get(username=serializer.data['comments_post'][i]['children_post'][ch]['user'])
                    # Отдельный комментарий преобразуем в словарь. затем добавляем в него аватар по модели юзера
                    serializer.data['comments_post'][i]['children_post'][ch] = dict(serializer.data['comments_post'][i]['children_post'][ch])
                    try:
                        serializer.data['comments_post'][i]['children_post'][ch]['avatar'] = Account.objects.get(user=user).avatar.url
                    except:
                        serializer.data['comments_post'][i]['children_post'][ch]['avatar'] = 'None'
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
        post = Posts.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data)
        user = request.user
        account = Account.objects.get(user=user)
        if serializer.is_valid() and user.is_authenticated and account.is_developer and post.author == user:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Posts.objects.get(id=pk)
        account = Account.objects.get(user=request.user)
        if account.is_developer and post.user == request.user:
            post.delete()
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
        posts = Posts.objects.get(id=request.data["id"])    # Ищем пост, к которому был оставлен коммент. По урлу.
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
        for i in range(int(request.data['imagesCount'])):     # Добавление картинок к игре
            if user.is_authenticated and account.is_developer:
                medias.append(Media.objects.create(img=request.data[f'images[{i}]'], author=user))
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid() and user.is_authenticated and account.is_developer:
            serializer.save(author=user, image=medias)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        game = self.get_game(pk)
        game.count_views += 1
        game.save()
        serializer = OutputGameSerializer(game)
        for i in range(len(serializer.data['reviews_game'])):
            # Получаем модель юзера по имени автора комментария
            user = User.objects.get(username=serializer.data['reviews_game'][i]['author'])
            try:
                # Отдельный комментарий преобразуем в словарь. затем добавляем в него аватар по модели юзера
                serializer.data['reviews_game'][i] = dict(serializer.data['reviews_game'][i])
                serializer.data['reviews_game'][i]['avatar'] = Account.objects.get(user=user).avatar.url
            except:
                serializer.data['reviews_game'][i] = dict(serializer.data['reviews_game'][i])
                serializer.data['reviews_game'][i]['avatar'] = 'None'
        num_views, create = Views_Game.objects.get_or_create(game=game, date=date.today())
        num_views.num += 1
        num_views.save()
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

    #def delete(self, request, pk):
    #    game = self.get_game(pk)
    #    account = Account.objects.get(user=request.user)
    #    if account.is_developer and game.author == request.user:
    #            game.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)


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
        title = request.POST.get('title')
        if comment:
            comment = Search.comments(Search(), comment)
        if title:
            title = Search.comments(Search(), title)
        serializer = ReviewSerializer(data={'author': user, 'mark': mark, 'game': pk,
                                            'comment': comment, 'title': title})
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
            user_ratings = Review.objects.filter(game=pk)
            serializer = []
            for i in user_ratings:
                serializer.append(dict(OutputReviewSerializer(i).data))
                user = User.objects.get(username=serializer[-1]['author'])  # Получаем модель пользователя по имени автора
                try:
                    serializer[-1]['avatar'] = Account.objects.get(user=user).avatar.url    # По модели юзера вытаскиваем аватарку из модели аккаунта и добавляем ее в словарь сериализатора
                except:
                    serializer[-1]['avatar'] = 'None'   # Если аватарки нет, указываем None
            return Response(serializer)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        game = self.get_game(pk)
        mark = request.POST.get('mark')
        user = request.user
        comment = request.POST.get('comment')
        comment = Search.comments(Search(), comment)
        title = request.POST.get('title')
        if user.is_authenticated:
            try:
                user_rating = Review.objects.get(author=user, game=pk)
            except Review.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = ReviewSerializer(user_rating, data={'author': user, 'mark': mark, 'game': pk,
                                                             'comment': comment, 'title': title})
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
    """Вывод новинок"""

    def get(self, request):
        games = Game.objects.filter(date_release__gte=date.today()-timedelta(days=7), is_hidden=False)\
            .order_by('-rating')[:4]
        serializer = OutputShortGameInfoSerializer(games, many=True)
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
                        game.count_players += 1
                        game.save()
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
                serializer = OutputShortGameInfoSerializer(games)
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
            serializer = OutputShortGameInfoSerializer(games, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class OutputWishlist(ListAPIView):
    """Вывод вишлиста пользователя"""

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            games = Game.objects.filter(who_added_to_wishlist=user, is_hidden=False)
            serializer = OutputShortGameInfoSerializer(games, many=True)
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
        games = Game.objects.filter(categories=category, is_hidden=False)
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


#class OutputGenre(ListAPIView):
    """Вывод списка жанров"""

    #def get(self, request):
    #    genres = Genre.objects.all()
    #    serializer = GenreSerializer(genres, many=True)
    #    return Response(serializer.data)


class OutputGenreGames(ListAPIView):

    def get(self, request, pk):
        games = Game.objects.filter(genre=pk, is_hidden=False).order_by('rating')
        serializer = OutputShortGameInfoSerializer(games, many=True)
        return Response(serializer.data)


class OutputGenreTopGames(ListAPIView):

    def get(self, request, pk):
        games = Game.objects.filter(genre=pk, is_hidden=False).order_by('rating')[:8]
        serializer = OutputShortGameInfoSerializer(games, many=True)
        return Response(serializer.data)

'''
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


class OutputStatistics(ListAPIView):
    """Вывод статистики разработчика (игра-рейтинг)"""

    def get(self, request, pk=0):
        user = request.user
        account = Account.objects.get(user=user)
        games = Game.objects.filter(author=user)
        orders = {}
        views_all = 0
        views_week = 0
        today = date.today()
        if user.is_authenticated and account.is_developer:
            serializer = StatisticsSerializer(games, many=True)
            if pk != 0:
                game = Game.objects.get(id=pk)
                if game.author == user:
                    for i in range(30):
                        orders[(today-timedelta(days=i)).strftime("%Y-%m-%d")] = Orders.objects.filter(game=game, date=today-timedelta(days=i)).count()
                    for i in Views_Game.objects.filter(game=game):
                        views_all += i.num
                    for i in range(7):
                        v, create = Views_Game.objects.get_or_create(game=game, date=today-timedelta(days=i))
                        views_week += v.num
                    wishlist = game.who_added_to_wishlist.all().count()
                    data = {'wishlist': wishlist, 'views_all': views_all, 'views_week': views_week, 'orders': orders, 'rating': list(serializer.data)}
                    return Response(data)
                return Response(status=status.HTTP_403_FORBIDDEN)
            data = {'rating': list(serializer.data)}
            return Response(data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
            game = Game.objects.filter(is_hidden=False)
            serializer = OutputGameSerializer(game, many=True)
        elif request.data['dir'] == 'news':
            post = Posts.objects.filter(draft=False)
            serializer = OutputAllNews(post, many=True)
        elif request.data['dir'] == 'library':
            user = request.user
            game = Game.objects.filter(players=user)
            serializer = OutputGameSerializer(game, many=True)
        elif request.data['dir'] == 'wishlist':
            user = request.user
            game = Game.objects.filter(who_added_to_wishlist=user, is_hidden=False)
            serializer = OutputGameSerializer(game, many=True)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        list_index = Search_engine(text, list(serializer.data))
        return Response(list_index)


class HideGameDetail(APIView):
    """Скрытие игры"""

    def post(self, request, pk):
        try:
            game = Game.objects.get(pk=pk)
            game.is_hidden = True
            game.save()
            return Response(status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ShowGameDetail(APIView):
    """Возвращение игры"""

    def post(self, request, pk):
        try:
            game = Game.objects.get(pk=pk)
            game.is_hidden = False
            game.save()
            return Response(status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GameInfoToEditDetail(ListAPIView):
    """Вывод информации по игре для последующего редактирования"""

    def get(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = OutputGameInfoToEditSerializer(game)
        user = request.user
        if user.is_authenticated and game.author == user:
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class RecommendedGamesDetail(ListAPIView):
    """Вывод рекомендуемых игр"""

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            bought_games = Game.objects.filter(players=user)
            if bought_games.count() > 0:
                genres = OrderedDict()
                for game in bought_games:
                    if game.genre in genres:
                        genres[game.genre] += 1
                    else:
                        genres[game.genre] = 1
                fav_genres = []
                all_genres = ['adventures', 'puzzles', 'action', 'rpg', 'strategy',
                              'farms', 'mmo', 'shooters', 'race', 'simulators']
                while len(genres) > 0 and len(fav_genres) <= 5:
                    fav_genres.append(list(genres.keys())[-1])
                    genres.pop(fav_genres[-1])
                recommended_games = Game.objects.exclude(players=user)
                for genre in all_genres:
                    if genre not in fav_genres:
                        recommended_games = recommended_games.exclude(genre=genre)
                recommended_games = recommended_games.order_by('rating')[:8]
                serializer = OutputShortGameInfoSerializer(recommended_games, many=True)
                return Response(serializer.data)
        recommended_games = Game.objects.all().order_by('rating')[:8]
        serializer = OutputShortGameInfoSerializer(recommended_games, many=True)
        return Response(serializer.data)


class BestGamesDetail(APIView):
    """
    Вывод бестселлеров (учитывается количество покупок за последний месяц)
    Выдается 5 самых покупаемых игр
    """

    def get(self, request):
        game = Game.objects.all()
        game_dict = {}
        serializer = []
        for i in game:
            orders = Orders.objects.filter(game=i, date__range=[date.today()-timedelta(days=30), date.today()]).count()
            if orders not in game_dict:
                game_dict[orders] = [i, ]
            else:
                game_dict[orders].append(i)
        for j in sorted(game_dict.keys(), reverse=True)[0:5]:
            for g in game_dict[j]:
                serializer.append(OutputShortGameInfoSerializer(g).data)
        return Response(serializer[0:5])


class PopularGamesDetail(APIView):
    """
    Вывод популярного (учитывается количество просмотров за последний месяц)
    Выдается 4 самых популярных игры
    """

    def get(self, request):
        game = Game.objects.all()
        game_dict = {}
        serializer = []
        for i in game:
            num = [i.num for i in Views_Game.objects.filter(game=i, date__range=[date.today()-timedelta(days=30), date.today()])]
            num = sum(num)
            if num not in game_dict:
                game_dict[num] = [i, ]
            else:
                game_dict[num].append(i)
        for j in sorted(game_dict.keys(), reverse=True)[0:4]:
            for g in game_dict[j]:
                serializer.append(OutputShortGameInfoSerializer(g).data)
        return Response(serializer[0:4])


class OutputDevelopersGames(ListAPIView):
    """Вывод игры на страницу "Мои игры" разработчика"""

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            games = Game.objects.filter(author=user)
            serializer = OutputDevelopersGamesInfoSerializer(games, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersAvatarDetail(APIView):
    """Загрузка аватарки пользователя"""

    def post(self, request):
        user = request.user
        avatar = request.data['avatar']
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            account.avatar = avatar
            account.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            try:
                return Response(account.avatar.url, status=status.HTTP_200_OK)
            except:
                return Response({"avatar": None})
        return Response(status=status.HTTP_400_BAD_REQUEST)