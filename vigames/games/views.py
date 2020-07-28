from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Account, Game
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

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


#в продакшене выпилить csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@csrf_exempt
def add_game(request):
    user = request.user
    if request.method == 'POST':
        data = {}
        data['message'] = ""
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            if account.is_developer:
                serializer = GameSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    data['message'] = "success"
            else:
                data['message'] = "не девелопер"

        else:
            data['message'] = "не аунтифицирован"
        return HttpResponse(data['message'])


@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def update_game(request, pk): #не работает
    user = request.user
    if request.method == 'PUT':
        data = {}
        data['message'] = "fail"
        if user.is_authenticated:
            account = Account.objects.get(user=user)
            if account.is_developer:
                if Game.objects.all().get in account.developed_games:
                    serializer = GameSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        data['message'] = "success"
        return HttpResponse(data['message'])



class GameView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
