from rest_framework import serializers
from .models import Account, Posts, Game, Comments_Post, Comments_Game, Review, FAQ, Orders, Media, \
    Question, Genre, Views_Game


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


class SerializerMedia(serializers.ModelSerializer):
    """Сериализатор изображений"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Media
        fields = ('img', 'author')


class OutputAllNews(serializers.ModelSerializer):
    """Вывод последних новостей на страницу news"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Posts
        fields = ('id', 'author', 'title', 'description', 'date', 'num_views', 'img')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор отдельного поста"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Posts
        exclude = ('fav', 'fav_date')


class OutputPost(PostSerializer):
    """Вывод отдельного поста"""

    comments_post = CommentsNewsSerializer(many=True)
    image = SerializerMedia(many=True)


class GameSerializer(serializers.ModelSerializer):
    """Сериализатор игры (нужен для добавления)"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Game
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор создания отзыва к игре"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class OutputReviewSerializer(serializers.ModelSerializer):
    """Сериализатор вывода отзывов к игре"""
    #account = AvatarSerializer(author, read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    #account = serializers.SlugRelatedField(slug_field='avatar', read_only=True)

    class Meta:
        model = Review
        fields = ('author', 'mark', 'game', 'title', 'comment')
        #fields = '__all__'


class OutputGameSerializer(serializers.ModelSerializer):
    """Сериализатор вывода игры на страницу"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    #comments_game = CommentsGameSerializer(many=True)
    reviews_game = ReviewSerializer(many=True)
    #players = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    #who_added_to_wishlist = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    categories = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    #genre = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    image = SerializerMedia(many=True)

    class Meta:
        model = Game
        fields = ('id', 'author', 'reviews_game', 'categories', 'genre', 'image', 'title', 'price', 'rating',
                  'description', 'short_description', 'is_hidden', 'img')


class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'title', 'rating', 'number_of_players')


class OutputShortGameInfoSerializer(serializers.ModelSerializer):
    """Сериализатор вывода игры в библиотеку, вишлист пользователя, на главную, на страницы жанров и т.д."""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    image = SerializerMedia(many=True)

    class Meta:
        model = Game
        fields = ('id', 'author', 'img', 'image', 'title', 'price', 'sale_percent', 'is_hidden')


class OutputDevelopersGamesInfoSerializer(serializers.ModelSerializer):
    """Сериализатор вывода игры на страницу "Мои игры" разработчика"""

    class Meta:
        model = Game
        fields = ('id', 'img', 'title', 'count_players', 'count_views', 'is_hidden')


class OutputGameInfoToEditSerializer(serializers.ModelSerializer):
    """Сериализатор вывода игры в библиотеку, вишлист пользователя, на главную, на страницы жанров и т.д."""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    image = SerializerMedia(many=True)

    class Meta:
        model = Game
        fields = ('id', 'author', 'img', 'banner', 'image', 'title', 'price', 'file',
                  'short_description', 'description', 'genre', 'is_hidden')


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


class ViewsGameSerializer(serializers.ModelSerializer):
    """ Сериализатор вывода количества просмотров игры """

    class Meta:
        model = Views_Game
        fields = "__all__"
