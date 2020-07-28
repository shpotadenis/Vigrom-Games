from rest_framework import serializers
from .models import Account, Posts, Game


#Сериализатор пользователя
class AccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'


class OutputAllNews(serializers.ModelSerializer):
    """Вывод последних новостей на страницу news"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Posts
        fields = ('author', 'title', 'description', 'data', 'url', 'num_views', 'img')

class OutputPost(serializers.ModelSerializer):
    """Вывод отдельного поста по url"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Posts
        exclude = ('draft', )

#Сериализатор игры
class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'

