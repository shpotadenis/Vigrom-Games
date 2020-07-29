from datetime import timedelta, date

from django.http import Http404
from djoser.conf import User
from rest_framework import status
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import Game
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, Posts
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import AccountSerializer, OutputAllNews, GameSerializer, OutputPost, CommentsNewsSerializer


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class OutputAllNewsView(APIView):
    """Вывод списка последних новостей"""

    def get(self, request):
        news = Posts.objects.filter(draft=False)
        serializer = OutputAllNews(news, many=True)
        return Response(serializer.data)

class OutputPostView(APIView):
    """ Вывод страницы записи"""

    def get(self, request, pk):
        news = Posts.objects.get(url=pk, draft=False)
        serializer = OutputPost(news)
        return Response(serializer.data)


class CommentCreateView(APIView):
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
        if serializer.is_valid():
            if user.is_authenticated:
                account = Account.objects.get(user=user)
                if account.is_developer:
                    serializer.save(author=account)
                    return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        game = self.get_game(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        game = self.get_game(pk)
        serializer = GameSerializer(game, data=request.data)
        user = request.user
        if serializer.is_valid():
            if user.is_authenticated:
                account = Account.objects.get(user=user)
                if account.is_developer:
                    if game.author == account:
                        serializer.save()
                        return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        game = self.get_game(pk)
        account = Account.objects.get(user=request.user)
        if account.is_developer:
            if game.author == account:
                game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OutputGames(ListAPIView):
    """Вывод списка игр за неделю"""

    def get(self, request):
        games = Game.objects.filter(date_release__gte=date.today() - timedelta(days=7)).order_by('-date_release')[:10]
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
