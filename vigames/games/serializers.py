from rest_framework import serializers
from .models import Account, Posts, Game, Comments_Post, Comments_Game, Rating


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


class CommentsNewsSerializer(serializers.ModelSerializer):
    """Вывод комментариев на странице новости"""

    class Meta:
        model = Comments_Post
        exclude = ('moderation', )


class CommentsGamesSerializer(serializers.ModelSerializer):
    """Вывод комментариев на странице игры"""

    class Meta:
        model = Comments_Game
        exclude = ('moderation', )


class OutputPost(serializers.ModelSerializer):
    """Вывод отдельного поста по url"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentsNewsSerializer(many=True)

    class Meta:
        model = Posts
        exclude = ('draft', )


#Сериализатор игры
class GameSerializer(serializers.ModelSerializer):
    #comments = CommentsGamesSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'