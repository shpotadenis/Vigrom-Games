from django.urls import include, path
from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('all-profiles', UserProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name="profile"),
]


#/api/accounts/all-profiles/	получить все профили пользователей и создать новый (не работает)
#/api/accounts/profile/id/	подробный вид профиля пользователя (не работает)
