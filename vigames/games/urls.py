from django.urls import include, path
from .views import UserProfileDetailView, OutputAllNewsView, OutputPostView

urlpatterns = [
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
    path('role/<int:pk>', UserProfileDetailView.as_view(), name="role"),

    path('news/', OutputAllNewsView.as_view()),
    path(('news/<str:pk>/'), OutputPostView.as_view())
]

#/api/accounts/profile/id/	редактирование аккаунта пользователя (изменение имени, фамилии, телефона и т.д.)
