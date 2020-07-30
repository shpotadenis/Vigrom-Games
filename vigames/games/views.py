from datetime import timedelta, date
from django.http import Http404
from rest_framework import status
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import Game, Rating, Account, Posts
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import AccountSerializer, OutputAllNews, GameSerializer, OutputPost, \
    RatingSerializer


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class OutputAllNewsView(APIView):
    """Вывод списка последних новостей"""

    def get(self, request):
        news = Posts.objects.filter(draft=False)
        serializer = OutputAllNews(news, many=True)


class OutputPostView(APIView):
    """ Вывод страницы записи"""

    def get(self, request, pk):
        news = Posts.objects.get(url=pk, draft=False)
        serializer = OutputPost(news)
        return Response(serializer.data)


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


class GameRatingDetail(APIView):

    def post(self, request, pk, format=None):
        user = request.user
        mark = request.POST.get('mark')
        rating_serializer = RatingSerializer(data={'author': user.id, 'mark': mark, 'game': pk})
        if rating_serializer.is_valid():
            if user.is_authenticated:
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
                account = Account.objects.get(user=user)
                if account not in game.players.all():
                    game.players.add(account)
                    return Response({"message": "success"}, status=status.HTTP_200_OK)
                return Response({"message": "bought"})
            except Account.DoesNotExist:
                return Response({"message": "fail"}, status=status.HTTP_400_BAD_REQUEST)
