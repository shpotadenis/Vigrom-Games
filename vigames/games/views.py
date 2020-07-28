from django.http import Http404
from rest_framework import status
from rest_framework.generics import (RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import Game
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Account, Posts
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import AccountSerializer, OutputAllNews, GameSerializer


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
                        serializer.save(author = account)
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