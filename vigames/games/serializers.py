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


class FilterCommentSerializer(serializers.ListSerializer):
    """Сериализатор, чтобы зависимые комментарии не дублировались в основном списке"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        print(data)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Сериализатор для вывода вложенных комментариев"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentsNewsSerializer(serializers.ModelSerializer):
    """Ввод/Вывод комментариев на странице новости"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comments_Post
        exclude = ('moderation', 'page')


class CommentsGamesSerializer(serializers.ModelSerializer):
    """Вывод комментариев на странице игры"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

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
