from rest_framework.generics import (RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import Account
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, Posts
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import AccountSerializer, OutputAllNews


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
