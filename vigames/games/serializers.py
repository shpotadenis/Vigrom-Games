from rest_framework import serializers
from .models import Account, Posts, Game, Comments_Post, Comments_Game, Review, FAQ, Orders, Media,\
    Question, Genre


class AccountSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'


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
    children_post = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comments_Post
        exclude = ('moderation', 'page')


class CommentsGameSerializer(serializers.ModelSerializer):
    """Ввод/Вывод комментариев на странице игры"""

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    children_game = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comments_Game
        exclude = ('moderation', 'page')


class OutputAllNews(serializers.ModelSerializer):
    """Вывод последних новостей на страницу news"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Posts
        fields = ('author', 'title', 'description', 'data', 'url', 'num_views', 'img')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор отдельного поста"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Posts
        fields = '__all__'


class OutputPost(PostSerializer):
    """Вывод отдельного поста по url"""

    comments_post = CommentsNewsSerializer(many=True)


class SerializerMedia(serializers.ModelSerializer):
    """Сериализатор изображений"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Media
        fields = ('img', 'author')


class GameSerializer(serializers.ModelSerializer):
    """Сериализатор игры (нужен для добавления)"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Game
        fields = '__all__'


class OutputGameSerializer(serializers.ModelSerializer):
    """Сериализатор вывода игры на страницу"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments_game = CommentsGameSerializer(many=True)
    #players = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    #who_added_to_wishlist = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    categories = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    image = SerializerMedia(many=True)

    class Meta:
        model = Game
        fields = ('author', 'comments_game', 'categories', 'genre', 'image', 'title', 'price', 'rating',
                  'description', 'short_description')


class GameLibrarySerializer(serializers.ModelSerializer):
    """Сериализатор вывода игры в библиотеку пользователя"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    image = SerializerMedia(many=True)

    class Meta:
        model = Game
        fields = ('id', 'author', 'img', 'image', 'title', 'price')


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзыва к игре"""

    class Meta:
        model = Review
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):
    """Сериализатор вопросов и ответов в Faq"""

    class Meta:
        model = FAQ
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор заказа (покупки) игры"""

    class Meta:
        model = Orders
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор вопросов к администраторам сайта"""

    class Meta:
        model = Question
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор жанров игр"""

    class Meta:
        model = Genre
        fields = '__all__'