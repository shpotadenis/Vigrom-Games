from django.urls import include, path
from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
