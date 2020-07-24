from rest_framework import serializers
from .models import Account, Posts


#Сериализатор пользователя
class AccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'


class OutputAllNews(serializers.ModelSerializer):
    """Вывод последних новостей на страницу news"""

    class Meta:
        model = Posts
        fields = ('author', 'title', 'description', 'data', 'urls', 'img', 'num_views')

