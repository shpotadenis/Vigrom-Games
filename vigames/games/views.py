from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, )
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
