from datetime import timedelta, date
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account, Posts, Game, Rating, Category, FAQ, Comments_Post, Comments_Game, Media
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import AccountSerializer, OutputAllNews, GameSerializer, OutputPost, \
    RatingSerializer, CommentsNewsSerializer, PostSerializer, FaqSerializer, CommentsGameSerializer, OrderSerializer, \
    OutputGameSerializer, QuestionSerializer, SerializerMedia
from django.contrib.auth.models import User

#class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    #queryset = Account.objects.all()
    #serializer_class = AccountSerializer
    #permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class OutputAllNewsView(APIView):
    """Вывод списка последних новостей"""

    def get(self, request):
        news = Posts.objects.filter(draft=False)
        serializer = OutputAllNews(news, many=True)
        return Response(serializer.data)


class AccountDetail(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(username=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): #отдавать не все параметры
        user = self.get_user(pk)
        account = Account.objects.get(user=user)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = request.user
        account = Account.objects.get(user=user)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid() and user.is_authenticated and user.username == pk:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = request.user
        if user.is_authenticated and user.username == pk:
                user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostView(APIView):
    """ Вывод страницы записи"""

    def get(self, request, pk):
        try:
            news = Posts.objects.get(url=pk, draft=False)
            serializer = OutputPost(news)
            return Response(serializer.data)
        except:
            raise Http404

    def post(self, request, format=None):
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

    def delete(self, request, pk, format=None):
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
        posts = Posts.objects.get(url=request.data["page"])    # Ищем пост, к которому был оставлен коммент. По урлу.
        if comment.is_valid() and user.is_authenticated:
            comment.save(user=user, page=posts)
            return Response(comment.data)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment = Comments_Post.objects.get(id=pk)
        serializer = CommentsNewsSerializer(comment, data=request.data)
        user = request.user
        if serializer.is_valid() and user.is_authenticated and comment.user == user:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
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
        print(request.data["page"])
        game = Game.objects.get(url=request.data["page"])    # Ищем пост, к которому был оставлен коммент. По урлу.
        if comment.is_valid() and user.is_authenticated:
            print(game)
            comment.save(user=user, page=game)
            return Response(comment.data)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment = Comments_Game.objects.get(id=pk)
        serializer = CommentsGameSerializer(comment, data=request.data)
        user = request.user
        if serializer.is_valid() and user.is_authenticated and comment.user == user:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = Comments_Game.objects.get(id=pk)
        if comment.user == request.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]


class GameDetail(APIView):

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        user = request.user
        serializer = GameSerializer(data=request.data)
        account = Account.objects.get(user=user)
        if serializer.is_valid() and user.is_authenticated and account.is_developer:
            serializer.save(author=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        game = self.get_game(pk)
        serializer = OutputGameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        game = self.get_game(pk)
        serializer = GameSerializer(game, data=request.data)
        user = request.user
        account = Account.objects.get(user=user)
        if serializer.is_valid() and user.is_authenticated and account.is_developer and game.author == user:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        game = self.get_game(pk)
        account = Account.objects.get(user=request.user)
        if account.is_developer and game.author == request.user:
                game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameRatingDetail(APIView):

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = request.user
        mark = request.POST.get('mark')
        rating_serializer = RatingSerializer(data={'author': user.id, 'mark': mark, 'game': pk})
        if rating_serializer.is_valid() and user.is_authenticated:
                user_ratings = Rating.objects.filter(author=user.id)
                flag = True
                for rating in user_ratings:
                    if rating.game.id == pk:
                        flag = False
                        break
                if flag:
                        rating_serializer.save()
                        return Response(rating_serializer.data)
        return Response(rating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        user = request.user
        data = None
        if user.is_authenticated:
            user_ratings = Rating.objects.filter(author=user.id)
            for rating in user_ratings:
                if rating.game.id == pk:
                    data = rating.mark
        return Response(data)

    def put(self, request, pk, format=None):
        game = self.get_game(pk)
        mark = request.POST.get('mark')
        user = request.user
        if user.is_authenticated:
            user_ratings = Rating.objects.filter(author=user.id)
            for rating in user_ratings:
                if rating.game.id == pk:
                    rating_ = rating
                    break
        serializer = RatingSerializer(rating_, data={'author': user.id, 'mark': mark, 'game': pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = request.user
        if user.is_authenticated:
            try:
                user_ratings = Rating.objects.get(author=user.id, game=pk)
            except Rating.DoesNotExist:
                user_ratings = None
            if user_ratings != None:
                user_ratings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OutputGames(ListAPIView):
    """Вывод списка игр за неделю"""
    def get(self, request):
        games = Game.objects.filter(date_release__gte=date.today()-timedelta(days=7))\
            .order_by('-date_release')[:10]
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class BuyGameDetail(APIView):

    def put(self, request, pk, format=None):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                #account = Account.objects.get(user=user)
                if user not in game.players.all():
                    game.players.add(user)
                    game.who_added_to_wishlist.remove(user)
                    price = game.price * game.sale_percent / 100
                    serializer = OrderSerializer(data={'user': user.id, 'game': pk, 'price': price, 'date': date.today()})
                    if serializer.is_valid():
                        serializer.save()
                    return Response({"message": "success"}, status=status.HTTP_200_OK)
                return Response({"message": "bought"})
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)


class WishListDetail(APIView):

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                #account = Account.objects.get(user=user)
                if user not in game.who_added_to_wishlist.all():
                    game.who_added_to_wishlist.add(user)
                    return Response({"message": "success"}, status=status.HTTP_200_OK)
                return Response({"message": "added"})
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                #account = Account.objects.get(user=user)
                if user in game.who_added_to_wishlist.all():
                    game.who_added_to_wishlist.remove(user)
            except Account.DoesNotExist:
                pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssessPostDetail(APIView):

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
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

    def delete(self, request, pk, format=None):
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

    def get(self, request, pk):
        user = request.user
        account = Account.objects.get(user=user)
        if user.username == pk:
            games = Game.objects.filter(players=user)
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data)
        #else:
        #выводить другие данные игры
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DownloadGame(ListAPIView):
    """Скачивание игры"""
    def get(self, request, pk):
        user = request.user
        game = Game.objects.get(id=pk)
        if user.is_authenticated:
            try:
                account = Account.objects.get(user=user)
                if account in game.players.all():
                    if game.file:
                        response = HttpResponse(game.file)
                        #надо заставлять разрабов загружать только зипы? сохранять имя и тип файла?
                        response['Content-Disposition'] = 'attachment; filename=' + game.title + '.zip'
                        return response
            except Account.DoesNotExist:
                return Response({"message": "fail"})
        return Response({"message": "fail"})


class GameCategoryDetail(ListAPIView):
    """Вывод игр соответствующей категории"""
    def get(self, request, pk):
        category = Category.objects.get(name=pk) #при прикручивании заюзать скрипт перевода в транслит(?)
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
