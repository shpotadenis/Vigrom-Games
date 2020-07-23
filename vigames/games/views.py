from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, )
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import AccountSerializer


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
